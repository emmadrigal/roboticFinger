package com.tec.emadrigal.keycode;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.TextView;


import org.w3c.dom.Text;

import java.util.Random;


public class MainActivity extends AppCompatActivity {

    Random randomGenerator;
    int currentNumber;
    int targetKeycode;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        randomGenerator = new Random();
        currentNumber = 0;

        final Button newKey = findViewById(R.id.newKey);
        newKey.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                targetKeycode = randomGenerator.nextInt(900000) + 100000;

                currentNumber = 0;

                TextView keycode = (TextView)findViewById(R.id.keyCode);
                keycode.setText(""+targetKeycode );

                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText("Inserted Keycode");
                insertedKeycode.setTextColor(Color.BLACK);//Black

            }
        });

        final Button button1 = findViewById(R.id.button1);
        button1.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 1;
                }


                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button2 = findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 2;
                }


                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button3 = findViewById(R.id.button3);
        button3.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 3;
                }

                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button4 = findViewById(R.id.button4);
        button4.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 4;
                }


                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button5 = findViewById(R.id.button5);
        button5.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 5;
                }


                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button6 = findViewById(R.id.button6);
        button6.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 6;
                }

                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                insertedKeycode.setTextColor(Color.GREEN);//Green
            }
            }
        });

        final Button button7 = findViewById(R.id.button7);
        button7.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 7;
                }

                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button8 = findViewById(R.id.button8);
        button8.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 8;
                }

                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button9 = findViewById(R.id.button9);
        button9.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10 + 9;
                }


                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });

        final Button button0 = findViewById(R.id.button0);
        button0.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(currentNumber < 100000){
                    currentNumber = currentNumber*10;
                }


                TextView insertedKeycode = (TextView)findViewById(R.id.insertedKeyCode);
                insertedKeycode.setText(""+currentNumber);

                if(currentNumber == targetKeycode){
                    insertedKeycode.setTextColor(Color.GREEN);//Green
                }
            }
        });
    }


    public void onRadioButtonClicked(View view) {
        // Is the button now checked?
        boolean checked = ((RadioButton) view).isChecked();

        // Check which radio button was clicked
        switch(view.getId()) {
            case R.id.layout1:
                if (checked) {
                    Button row1= (Button) findViewById(R.id.button1);
                    Button row2= (Button) findViewById(R.id.button4);
                    Button row3= (Button) findViewById(R.id.button7);

                    row1.setMinHeight(150);
                    row2.setMinHeight(150);
                    row3.setMinHeight(150);

                    break;
                }
            case R.id.layout2:
                if (checked) {
                    Button row1= (Button) findViewById(R.id.button1);
                    Button row2= (Button) findViewById(R.id.button4);
                    Button row3= (Button) findViewById(R.id.button7);

                    row1.setMinHeight(300);
                    row2.setMinHeight(300);
                    row3.setMinHeight(300);
                    break;
                }
            case R.id.layout3:
                if (checked) {
                    Button row1= (Button) findViewById(R.id.button1);
                    Button row2= (Button) findViewById(R.id.button4);
                    Button row3= (Button) findViewById(R.id.button7);

                    row1.setMinHeight(400);
                    row2.setMinHeight(400);
                    row3.setMinHeight(400);
                    break;
                }
        }
    }

}

//TODO check when correct code is inputed

//TODO change width??
