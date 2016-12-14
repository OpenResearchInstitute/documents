JSONArray payload;
import java.util.Date;
int xPos=200;
PFont f;
int daylength = 24*60*60;

void setup()
{
  payload = loadJSONArray("WeatherMapTestObject.txt"); 
  //payload database is loaded into a JSON array object
  //Here's what the JSON file looks like:
  //[
  //{
  //"lastheard":1480622876,
  //"callsign":"w5nyv",
  //"ssid":"",
  //"modcod":"218",
  //},
  //{
  //"lastheard": 1478301018,
  //"callsign":"kb5mu",
  //"ssid":"-7",
  //"modcod":"6",
  //}
  //]

  
  
  Date d = new Date();
  long current = d.getTime()/1000; 
  println("current time is", current);

  
  
  
  
  long freshness;
  
  //QPSK 4/15 (identification number 218) -2.24
  //QPSK 2/5 (identification number 3) 0
  //QPSK 2/3 (identification number 6) 2.8
  //QPSK 4/5 (identification number 8) 4.38
  //8PSK 5/6 (identification number 15) 7.7
  //8PSK 8/9 (identification number 16) 10.4  
  //modcod_list = new IntDict();
  //println(modcod_list);
  
  size(800, 300);
  background(255);    // Setting the background to white
  stroke(0);          // Setting the outline (stroke) to black
  
  f = createFont("Arial",18,true); // STEP 2 Create Font
  textFont(f,12);                  // STEP 3 Specify font to be used

  
  println("Payload size is", payload.size());
     
  for (int i = 0; i < payload.size(); i++) 
  {
    //loop through each element of the JSON array by using the payload.size() function
     JSONObject operator = payload.getJSONObject(i);
     //get the array element for this loop. Each element of the array is an operator. 
     long lastheard = operator.getInt("lastheard"); //if never operated, this is timestamp of registration
     //get the element lastheard which is the timestamp of the last time they were on the system
     //timestamp is UNIX timestamp format.
     freshness = current - lastheard;
     //freshness is the difference between the current time and the time they were last heard on the system
     String callsign = operator.getString("callsign");
     //get the callsign
     String ssid = operator.getString("ssid");
     //get the SSID. There might not be an SSID
     String location = "Maidenhead Grid Square";
     //get their grid location. It's either live or based off the address of their call sign
     int my_modcod = operator.getInt("modcod");
     //get their modulation and coding index number
     operator.setString("grid", location);
     

   
     fill(freshness_level(freshness));// Setting the interior of a shape (fill) to grey
     rect(   (50 + 70*i ),(250), 50, -(50+modulation_level(my_modcod)*30)); // Drawing the rectangle
     fill(0);
     text(callsign + ssid, (50 + 70*i), 275); 
     
     if (ssid.equals("") == true){
       //println(callsign + " was last heard at " + lastheard + ". hotness of " + freshness);
     }
     else{
       //println(callsign + ssid + " was last heard at " + lastheard + ". hotness of " + freshness);
     }
     
    
  }
  
  
  
  
  saveJSONArray(payload, "WeatherMapModified.txt");  
}







//function input is freshness. This is how many seconds ago station was heard.
//function returns a gray value that we can use on our graphical display.
int freshness_level(long my_freshness){
  long grayvalue;
  long check_value = 7*24*60*60; //how many seconds in a week
  println("inside function freshness level is", my_freshness);
  println("inside function, check level is", check_value);
  if (my_freshness > check_value){
    println("more than a week old!");
    grayvalue = 255; //white is empty, expired. Black is most recently heard. 
  }
  else{
  //map check_value (timestamp is a week or less) to 255
  grayvalue = ((my_freshness*255/check_value));
  }
  println("gray level is", grayvalue);
  return int(grayvalue);
}


int modulation_level(int my_modcod){
  //QPSK 4/15 (identification number 218) -2.24
  //QPSK 2/5 (identification number 3) 0
  //QPSK 2/3 (identification number 6) 2.8
  //QPSK 4/5 (identification number 8) 4.38
  //8PSK 5/6 (identification number 15) 7.7
  //8PSK 8/9 (identification number 16) 10.4
  int[] modcod_list = {218, 3, 6, 8, 15, 16 };
  int index_i = 0;
  //println("modulation code is", my_modcod);
  for (int i = 0; i < modcod_list.length; i++) {
    if (modcod_list[i] == my_modcod){
      index_i = i;
      //println("the modulation graphical offset is",i);
    }
  }
  return index_i;
}

//String grid_square(){
 
//For simplicity, let's assume that West and South are negative lat/long, 
//as is a common convention. For example purposes, I'm going to use 32.123 W, 14.321 N. 
//The key thing is to do the following.:

//Longitude

//Add 180 to the longitude, and take the integer value /20, and add one. 
//Then figure out which letter of the alphabet that corresponds to, usually written in upper case. 
//The example will be 147.877/20=7. Adding one will give the 8th letter of the alphabet, or H. Note 7.877 is remaining.
//Take the remainder of what is left, and divide by 2, rounding down. This is the number, no conversion required. 
//The example will give a value of 3. Note 1.877 is remaining.
//Take the remainder that is left, and multiply by 12, and add one. Round down to the nearest integer.. 
//This is the letter of the alphabet, usually written in lower case. The example gives a value of 22+1=23. This will be the letter w.

//Latitude

//Add 90 to the longitude, and take the integer value /10, and add one. 
//Then figure out which letter of the alphabet that corresponds to, usually written in upper case. 
//The example will be 104.321/10=10. Adding one will give the 11th letter of the alphabet, or K. Note 4.321 is remaining.
//Take the remainder of what is left, and round down. This is the number, no conversion required. 
//The example will give a value of 4. Note 0.321 is remaining.
//Take the remainder that is left, and multiply by 24, and add one. 
//Round down to the nearest integer.. This is the letter of the alphabet, usually written in lower case. 
//The example gives a value of 7+1=8. This will be the letter h.
  
  
 
  
  
  
//}