float[][] front;
float[][] window;
float[][] fender;
float[][] head;
float[][] grill;
float[][] bumper;

int count=0;

float[][] s1;
float[][] s2;
float[][] s3;
float[][] s4;
float[][] s5;
float[][] s6;
float[][] s7;
float[][] s8;

float[][] b1;
float[][] b2;
float[][] b3;
float[][] b4;
float[][] b5;

float[][] t1;
float[][] t2;
float[][] t3;
float[][] t4;
float[][] t5;
float[][] t6;
float[][] t7;
float[][] t8;
float[][] t9;
float[][] t10;

float tm,tM;
String[] lines;
String[] lines2;
String[] lines3;
String[] lines4;
String[] lines5;
String[] lines6;

String[] lines21;
String[] lines22;
String[] lines23;
String[] lines24;
String[] lines25;
String[] lines26;
String[] lines27;
String[] lines28;

String[] lines31;
String[] lines32;
String[] lines33;
String[] lines34;
String[] lines35;

String[] lines41;
String[] lines42;
String[] lines43;
String[] lines44;
String[] lines45;
String[] lines46;
String[] lines47;
String[] lines48;
String[] lines49;
String[] lines410;

void setup(){
  size(1500,800);
  lines=loadStrings("1_1.txt");
  lines2=loadStrings("1_2.txt");
  lines3=loadStrings("1_3.txt");
  lines4=loadStrings("1_4.txt");
  lines5=loadStrings("1_5.txt");
  lines6=loadStrings("1_9.txt");
  
  
  lines21=loadStrings("2_1.txt");
  lines22=loadStrings("2_2.txt");
  lines23=loadStrings("2_3.txt");
  lines24=loadStrings("2_4.txt");
  lines25=loadStrings("2_5.txt");
  lines26=loadStrings("2_6.txt");
  lines27=loadStrings("2_7.txt");
  lines28=loadStrings("2_8.txt");
  
  lines31=loadStrings("3_1.txt");
  lines32=loadStrings("3_2.txt");
  lines33=loadStrings("3_3.txt");
  lines34=loadStrings("3_4.txt");
  lines35=loadStrings("3_6.txt");
  
  
  lines41=loadStrings("4_1.txt");
  lines42=loadStrings("4_2.txt");
  lines43=loadStrings("4_3.txt");
  lines44=loadStrings("4_4.txt");
  lines45=loadStrings("4_5.txt");
  lines46=loadStrings("4_6.txt");
  lines47=loadStrings("4_7.txt");
  lines48=loadStrings("4_8.txt");
  lines49=loadStrings("4_9.txt");
  lines410=loadStrings("4_0.txt");
  
  
  
  front = new float[lines.length][2];
  for(int i=0;i<lines.length;i++){
    String[] pieces = split(lines[i],' ');
    front[i][0]=float(pieces[0]);
    front[i][1]=float(pieces[1]);    
  }
  
  
  window = new float[lines2.length][2];
  for(int i=0;i<lines2.length;i++){
    String[] pieces = split(lines2[i],' ');
    window[i][0]=float(pieces[0]);
    window[i][1]=float(pieces[1]);    
  }
  
  fender = new float[lines3.length][2];
  for(int i=0;i<lines3.length;i++){
    String[] pieces = split(lines3[i],' ');
    fender[i][0]=float(pieces[0]);
    fender[i][1]=float(pieces[1]);    
  }
  
  head = new float[lines4.length][2];
  for(int i=0;i<lines4.length;i++){
    String[] pieces = split(lines4[i],' ');
    head[i][0]=float(pieces[0]);
    head[i][1]=float(pieces[1]);    
  }
  
  grill = new float[lines5.length][2];
  for(int i=0;i<lines5.length;i++){
    String[] pieces = split(lines5[i],' ');
    grill[i][0]=float(pieces[0]);
    grill[i][1]=float(pieces[1]);    
  }
  
  bumper = new float[lines6.length][2];
  for(int i=0;i<lines6.length;i++){
    String[] pieces = split(lines6[i],' ');
    bumper[i][0]=float(pieces[0]);
    bumper[i][1]=float(pieces[1]);    
  }
  
  
  s1 = new float[lines21.length][2];
  for(int i=0;i<lines21.length;i++){
    String[] pieces = split(lines21[i],' ');
    s1[i][0]=float(pieces[0]);
    s1[i][1]=float(pieces[1]);    
  }
  
  s2 = new float[lines22.length][2];
  for(int i=0;i<lines22.length;i++){
    String[] pieces = split(lines22[i],' ');
    s2[i][0]=float(pieces[0]);
    s2[i][1]=float(pieces[1]);    
  }
  s3 = new float[lines23.length][2];
  for(int i=0;i<lines23.length;i++){
    String[] pieces = split(lines23[i],' ');
    s3[i][0]=float(pieces[0]);
    s3[i][1]=float(pieces[1]);    
  }
  s4 = new float[lines24.length][2];
  for(int i=0;i<lines24.length;i++){
    String[] pieces = split(lines24[i],' ');
    s4[i][0]=float(pieces[0]);
    s4[i][1]=float(pieces[1]);    
  }
  s5 = new float[lines25.length][2];
  for(int i=0;i<lines25.length;i++){
    String[] pieces = split(lines25[i],' ');
    s5[i][0]=float(pieces[0]);
    s5[i][1]=float(pieces[1]);    
  }
  s6 = new float[lines26.length][2];
  for(int i=0;i<lines26.length;i++){
    String[] pieces = split(lines26[i],' ');
    s6[i][0]=float(pieces[0]);
    s6[i][1]=float(pieces[1]);    
  }
  s7 = new float[lines27.length][2];
  for(int i=0;i<lines27.length;i++){
    String[] pieces = split(lines27[i],' ');
    s7[i][0]=float(pieces[0]);
    s7[i][1]=float(pieces[1]);    
  }
  s8 = new float[lines28.length][2];
  for(int i=0;i<lines28.length;i++){
    String[] pieces = split(lines28[i],' ');
    s8[i][0]=float(pieces[0]);
    s8[i][1]=float(pieces[1]);    
  }
  
  
  b1 = new float[lines31.length][2];
  for(int i=0;i<lines31.length;i++){
    String[] pieces = split(lines31[i],' ');
    b1[i][0]=float(pieces[0]);
    b1[i][1]=float(pieces[1]);    
  }
  
  b2 = new float[lines32.length][2];
  for(int i=0;i<lines32.length;i++){
    String[] pieces = split(lines32[i],' ');
    b2[i][0]=float(pieces[0]);
    b2[i][1]=float(pieces[1]);    
  }
  b3 = new float[lines33.length][2];
  for(int i=0;i<lines33.length;i++){
    String[] pieces = split(lines33[i],' ');
    b3[i][0]=float(pieces[0]);
    b3[i][1]=float(pieces[1]);    
  }
  b4 = new float[lines34.length][2];
  for(int i=0;i<lines34.length;i++){
    String[] pieces = split(lines34[i],' ');
    b4[i][0]=float(pieces[0]);
    b4[i][1]=float(pieces[1]);    
  }
  b5 = new float[lines35.length][2];
  for(int i=0;i<lines35.length;i++){
    String[] pieces = split(lines35[i],' ');
    b5[i][0]=float(pieces[0]);
    b5[i][1]=float(pieces[1]);    
  }
  t1 = new float[lines41.length][2];
  for(int i=0;i<lines41.length;i++){
    String[] pieces = split(lines41[i],' ');
    t1[i][0]=float(pieces[0]);
    t1[i][1]=float(pieces[1]);    
  }
  
  t2 = new float[lines42.length][2];
  for(int i=0;i<lines42.length;i++){
    String[] pieces = split(lines42[i],' ');
    t2[i][0]=float(pieces[0]);
    t2[i][1]=float(pieces[1]);    
  }
  
  t3 = new float[lines43.length][2];
  for(int i=0;i<lines43.length;i++){
    String[] pieces = split(lines43[i],' ');
    t3[i][0]=float(pieces[0]);
    t3[i][1]=float(pieces[1]);    
  }
  t4 = new float[lines44.length][2];
  for(int i=0;i<lines44.length;i++){
    String[] pieces = split(lines44[i],' ');
    t4[i][0]=float(pieces[0]);
    t4[i][1]=float(pieces[1]);    
  }
  t5 = new float[lines45.length][2];
  for(int i=0;i<lines45.length;i++){
    String[] pieces = split(lines45[i],' ');
    t5[i][0]=float(pieces[0]);
    t5[i][1]=float(pieces[1]);    
  } 
  t6 = new float[lines46.length][2];
  for(int i=0;i<lines46.length;i++){
    String[] pieces = split(lines46[i],' ');
    t6[i][0]=float(pieces[0]);
    t6[i][1]=float(pieces[1]);    
  }
  t7 = new float[lines47.length][2];
  for(int i=0;i<lines47.length;i++){
    String[] pieces = split(lines47[i],' ');
    t7[i][0]=float(pieces[0]);
    t7[i][1]=float(pieces[1]);    
  }
  t8 = new float[lines48.length][2];
  for(int i=0;i<lines48.length;i++){
    String[] pieces = split(lines48[i],' ');
    t8[i][0]=float(pieces[0]);
    t8[i][1]=float(pieces[1]);    
  }
  t9 = new float[lines49.length][2];
  for(int i=0;i<lines49.length;i++){
    String[] pieces = split(lines49[i],' ');
    t9[i][0]=float(pieces[0]);
    t9[i][1]=float(pieces[1]);    
  }
  t10 = new float[lines410.length][2];
  for(int i=0;i<lines410.length;i++){
    String[] pieces = split(lines410[i],' ');
    t10[i][0]=float(pieces[0]);
    t10[i][1]=float(pieces[1]);    
  }

  
}

void draw(){
 background(0); 
 stroke(255);
 noFill();
 if(count<0){
 text(count,100,100);
 }else if(count<5){
   text("front",100,70);
   text(count,100,100);
 }else if(count==5){
   text("front",100,70);
   text("9",100,100);
 }else if(count<14){
   text("side",100,70);
   text(count-5,100,100);
 }else if(count<18){
   text("back",100,70);
   text(count-13,100,100);
 }else if(count==18){
   text("back",100,70);
   text("6",100,100);
 }else if(count<28){
   text("top",100,70);
   text(count-18,100,100);
 }else if(count==28){
   text("top",100,70);
   text("0",100,100);
 }else{
   text(count,100,100);
 }
 translate(1000,height/2);
 if(count==0){
  stroke(255,0,0); 
 }
 beginShape();
 for(int i=0;i<lines.length;i++){
 vertex(front[i][0],-front[i][1]);
 }
 endShape(CLOSE);
 stroke(255);
 
 if(count==3){
  stroke(255,0,0); 
 }
 beginShape();
 for(int i=0;i<lines4.length;i++){
 vertex(head[i][0],-head[i][1]);
 }
 endShape(CLOSE);
 stroke(255);
 
 
 
 if(count==6){
  stroke(255,0,0); 
 }
 beginShape();
 for(int i=0;i<lines21.length;i++){
 vertex(s1[i][0],-s1[i][1]);
 }
 endShape(CLOSE);
 stroke(255);
 
 if(count==11){
  stroke(255,0,0); 
 }
 beginShape();
 for(int i=0;i<lines26.length;i++){
 vertex(s6[i][0],-s6[i][1]);
 }
 endShape(CLOSE);
 stroke(255);
  line(-626,-74,34,-93);
 line(-626,-74,-269,-11);
 line(-626,-74,-277,8);
 line(-626,-74,-281,61);
 if(mousePressed){
  line(-626,-74,mouseX-1000,mouseY-(height/2));
 }  
 
 
}


void keyPressed(){
 if(keyCode==UP){
  count++;
 }else if(keyCode==DOWN){
  count--; 
 }
  
}


void mousePressed(){
  int tempX=mouseX-1000;
  int tempY=mouseY-(height/2);
  println(tempX+","+tempY);
}
void mouseReleased(){
  int tempX=mouseX-1000;
  int tempY=mouseY-(height/2);
  println(tempX+","+tempY);
}

