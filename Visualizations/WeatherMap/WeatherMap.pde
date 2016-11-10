JSONArray payload;
import java.util.Date;
int xPos=200;
PFont f;

void setup()
{
  payload = loadJSONArray("WeatherMapTestObject.txt");
  Date d = new Date();
  long current = d.getTime()/1000; 
  //println("current time is", current);
  long freshness;
  
  //QPSK 4/15 (identification number 218) -2.24
  //QPSK 2/5 (identification number 3) 0
  //QPSK 2/3 (identification number 6) 2.8
  //QPSK 4/5 (identification number 8) 4.38
  //8PSK 5/6 (identification number 15) 7.7
  //8PSK 8/9 (identification number 16) 10.4  modcod_list = new IntDict();
  //println(modcod_list);
  
  size(800, 300);
  background(255);    // Setting the background to white
  stroke(0);          // Setting the outline (stroke) to black
  
  f = createFont("Arial",18,true); // STEP 2 Create Font
  textFont(f,12);                  // STEP 3 Specify font to be used

  
     
  for (int i = 0; i < payload.size(); i++) 
  {
     JSONObject operator = payload.getJSONObject(i);
     long lastheard = operator.getInt("lastheard"); //if never operated, this is timestamp of registration
     freshness = current - lastheard;
     String callsign = operator.getString("callsign");
     String ssid = operator.getString("ssid");
     String location = "Maidenhead Grid Square";
     int my_modcod = operator.getInt("modcod");
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
  
  
  
  
  saveJSONArray(payload, "WeatherMapModified");  
}








int freshness_level(long my_freshness){
  long grayvalue;
  long check_value = 7*24*60*60;
  //println("freshness level is", my_freshness);
  //println("check level for a week is", check_value);
  if (my_freshness > check_value){
    //println("more than a week old!");
    grayvalue = 255;
  }
  else{
  //map check_value (timestamp is a week or less) to 255
  grayvalue = ((my_freshness*255/check_value));
  }
  //println("gray level is", grayvalue);
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