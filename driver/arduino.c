/**
 * 
 * Arduino Control Driver
 * 
 * This driver is in charge of sending data to the arduino through
 * the serial port
 * 
 * @author Jonatan Chaverri, Emmanuel Madrigal & Mauricio Montero
 * 
 */


#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/slab.h> /* kmalloc() */

#include <linux/fs.h>
#include <asm/segment.h>
#include <asm/uaccess.h>
#include <linux/buffer_head.h>


MODULE_LICENSE("Dual BSD/GPL");


//////////////////////////////////
//File operations
//////////////////////////////////

/*
 * This function opens a file
 * 
 * @param path to the to be opened
 * @param flags open flags, must include one of the following: O_RDONLY, O_WRONLY, or O_RDWR
 * @param rights to set if the O_CREAT or O_TMPFILE is set
 * 
 * @return pointer to file structure
 */
struct file *file_open(const char *path, int flags, int rights) 
{
	struct file *filp = NULL;
	mm_segment_t oldfs;
	int err = 0;

	oldfs = get_fs();
	set_fs(get_ds());
	filp = filp_open(path, flags, rights);
	set_fs(oldfs);
	if (IS_ERR(filp)) {
		err = PTR_ERR(filp);
		return NULL;
	}
	return filp;
}

/*
 * Closes a file
 * 
 * @param pointer to the file to be closed
 * 
 */
void file_close(struct file *file) 
{
	filp_close(file, NULL);
}

/*
 * Reads data from a file
 * 
 * @param file pointer to file structure
 * @param offset from where to start reading
 * @param pointer where data will be read
 * @param how many bytes wil be read
 * 
 */
int file_read(struct file *file, unsigned long long offset, unsigned char *data, unsigned int size) 
{
	mm_segment_t oldfs;
	int ret;

	oldfs = get_fs();
	set_fs(get_ds());

	ret = vfs_read(file, data, size, &offset);

	set_fs(oldfs);
	return ret;
}   

/*
 * Writes data to a file
 * 
 * @param pointer to file descriptor
 * @param offest from where writing will start
 * @param data from where the data will be written
 * @param size how many files will be read
 * 
 * @return int 0 if succesfull, error code otherwise
 * 
 */
int file_write(struct file *file, unsigned long long offset, unsigned char *data, unsigned int size) 
{
	mm_segment_t oldfs;
	int ret;

	oldfs = get_fs();
	set_fs(get_ds());

	ret = vfs_write(file, data, size, &offset);

	set_fs(oldfs);
	return ret;
}

/*
 * Commits file caches to disk
 * 
 * @param file descriptor
 * 
 * @return 0
 */
int file_sync(struct file *file) 
{
	vfs_fsync(file, 0);
	return 0;
}


//////////////////////////////////
//Arduino Kernel Module File Operations
//////////////////////////////////


static int hello_init(void) {
	printk("\tLoading arduino LKM\n");
	
	struct file *test = file_open("/tmp/text.txt", O_WRONLY, 777) ;
	
	printk("\t TEST: %p\n", test);
	
	unsigned char data[25] = "Hello from Kernel Space\n";
	
	
	unsigned long long  pos = 0;
	int a = file_write(test, pos, data, 25);
	
	printk("\t TEST: %d\n", a);
	
	file_sync(test);
	
	file_close(test);
	
	kfree(data);
	
	printk("\tSupposedly writing is done\n");
	
	return 0;
}

static void hello_exit(void) {
	printk("\tUnloading arduino LKM\n");
}

module_init(hello_init);
module_exit(hello_exit);