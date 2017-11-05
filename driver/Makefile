obj-m := arduino.o


SRC := $(PWD)
all:
		$(MAKE) -C /usr/src/linux-headers-$(shell uname -r) M=$(SRC)
modules_install:
		$(MAKE) -C /usr/src/linux-headers-$(shell uname -r) M=$(SRC) modules_install
clean:
		rm -f *.o *~ core .depend .*.cmd *.ko *.mod.c
		rm -f Module.markers Module.symvers modules.order
		rm -rf .tmp_versions Modules.symvers