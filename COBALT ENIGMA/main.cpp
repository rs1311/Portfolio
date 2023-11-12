//CobaltEnigma Final Script
//Authored by Safe.Ducks & RR2000
//HackNRoll 2020







//Library Declarations
#include <iostream>
#include <random>
#include <string>
#include <unistd.h>
#include <sys/time.h>
#include <thread>


//(Standard)Namespace STD
using namespace std;



//Variable Declarations - Account Info & Special
int game;
string cont;
string name;
string password;
string passcodenew;
string a;
string cf;
string cc;



//RNG Challenge Variables
int n1;
int a1;
int chances;


//Cipher input
string trans_input;
string caesar_input;
string morse_input;
string nual_input;
string nato_input;



//Cipher key
string trans;
string caesar;
string morse;
string nual;
string nato;










//Fast Typing Animation Function Declaration
void type_text_fast (const string& text)
{
    
    for (size_t i = 0; i < text.size(); ++i)
    {
        
        std::cout << text[i] << std::flush;

        // sleep 60 milliseconds
        this_thread::sleep_for(chrono::milliseconds(100));
    }
}



//Slow Typing Animation Function Declaration
void type_text_slow (const string& text)
{
    
    for (size_t i = 0; i < text.size(); ++i)
    {
        
        std::cout << text[i] << std::flush;

        // sleep 60 milliseconds
        this_thread::sleep_for(chrono::milliseconds(250));
    }
}



//Typing Animation Function Declaration
void type_text(const string& text)
{
    
    for (size_t i = 0; i < text.size(); ++i)
    {
        
        std::cout << text[i] << std::flush;

        // sleep 60 milliseconds
        this_thread::sleep_for(chrono::milliseconds(120));
    }
}










//Clearing the screen
void clear(){
  sleep (1);
  cout<<" \033[2J\033[0;0H \n";
  sleep (1);
}










//Main Code
int main (){
  game=0;





  while (game!=1){

    clear ();
    
    //Value Declarations
    trans="silver";
    caesar="iodine";
    morse="tantalum";
    nual="titanium";
    nato="oxygen";
    chances=7;





    //Producing the RNG
    srand((unsigned)time(0)); 
    n1 = (rand()%10)+1; 







    //..........................
   //Virtual Output has begun
    //..........................







    //Item Requirements & Preparation
    //Instruction Welcome
    type_text("Welcome to Cobalt Enigma!\n\a");
    sleep (3);

    //Instruction Welcome 2
    cout<<"Before we start our game, here are some useful links. \n\n";
    sleep(2);

    //Translation Guide
    cout<<"For Translation : \n";
    sleep (1);
    type_text("translate.google.com \n\n");
    sleep(1);

    //Crypto Guide
    cout<<"For Encoding/Decoding :  \n";
    sleep (1);
    type_text("cryptii.com \n\n");
    sleep(1);

    //Periodic Table Guide
    cout<<"For The Periodic Table of Elements : \n";
    sleep (1);
    type_text("ptable.com \n\n");
    sleep(1);

    //Notepad Guide
    cout<<"You might also need a notepad, or document application \n\n";
    sleep (5);

    //Input Confirmation
    cout<<"Input anything to continue, once you are ready! \n\a";
    cin>>a;
    sleep (3);





    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    clear();










    //******************************************
    //*****THE GAME HAS OFFICIALLY STARTED *****
    //******************************************










    //Title Sequence
    type_text_slow("C\aO\aB\aA\aL\aT\a E\aN\aI\aG\aM\aA\a \n");
    sleep (2);
    type_text_fast("Authored by Madhan Selvaraj and Raghav Sriram");
    sleep (2);





    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    sleep (2);
    clear();
    sleep (2);





    //Waking up
    type_text_fast ("You wake up abruptly.\n Once the brightness of the area sets in, you begin to feel conscious.\n You squint your eyes, and realise that you are trapped inside some sort of pod.\n Wires connect the chamber to a metallic box, with flashing lights and buttons.\n Noting these surroundings, you push on the door of the pod instinctively.\n It opens, and you climb out.\n Your knees buckle, and you fall to the floor.\n Weakness and nausea spread throughout your being.\n You stagger to the end of the room, where a computer is.\n");
    sleep (3);
    cout<<"Press any key to acess the computer\n";
    cin>>a;





    //Access the Computer
    clear ();
    type_text_fast("You pull a chair under you and peer into the dusty monitor. You instintively power the computer on. Text fills the screen.\n");
    sleep (4);
    clear();




    //Recording User Data
    sleep (1);
    cout<<"Account Login\a\n Username: ";
    cin>>name;
    cout<<" Password\a: \n\n\n";
    sleep (1);
    type_text("Somehow, the passcode is in your memory right now. It could be anything, but you must know it. You think about typing something only you know. You reach into your memory and pull out an answer. You type it: \n\n\n");
    cin>>password;





    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    clear();




  
    //Logging on animation
    cout<<"Logging on...\n";
    sleep (1);





    //ClearScreen:::::::::::::::::::::::::::::::::::::::
    clear();





    //Computer Startup
    cout<<"Welcome, " << name << " \n\a";
    sleep(1);





    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    clear();





    //ChemLab Database Visual-Only
    cout<<"Welcome to the Chemical Laborotary Database.\n";
    sleep (2);
    cout<<"Please Enter Your Key\n";





    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    clear();





    //RNG Game Introduction
    cout<<"\a!!Fatal System Error!!: \n\n To Access the Chemical Laboratory Database, a key is needed. \n The saved key has been disconnected. \n Please manually search the directories and logs for the key, or information backed up about the key in a text (.txt) file.\n Search for the Text File only, as there is also system UI clutter.\n";





    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    sleep (9);
    clear();





    //RNG Game Introduction Pt2
    cout<< "\a!Interface Error!: \n\n SYSTEM SECURITY ERROR. \n CLOSING DIRECTORIES AND LOGS...\n\n\n PLEASE SAVE IMPORTANT DATA NOW...\n\n\n\n";





    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    sleep (4);
    clear ();





    //RNG Game Opening
    cout<<"SYSTEM DIRECTORY RECOVERY.exe \n There are *10* Directories.  Which directory ID *1* - *10* would you like to call?\n";
    cin>>a1;





    //RNG Game 
    while (chances>0){
      if(a1==n1){





        //The correct directory is called
        cout<<"\aText File : chemlabkey.txt \n"; 
        cout<<"Contents : Personal Mail \n ";
        cout<<"Dear Mr Steven, \n"  ;
        cout<<"Firstly, we congratulate you on your success in getting into the royal association.\n"; 
        cout<<" You have been assigned to the Chemical Laboratory.\n";
        cout<<"Your key is \n" ;
        cout<<"*cobalt*\n" ;
        cout<<"This is classified information, do not share this with anyone.\n";





        //ScreenClear:::::::::::::::::::::::::::::::::::::
        sleep (10);
        clear();
        chances=0;





      }
      else{





        //The wrong directory is called
        cout<<"*****************************************\n";
        cout<<"*System File : windows_8.1_system_ui.exe*\n";
        cout<<"*Contents : Software Application        *\n";
        cout<<"*****************************************\n";
      



        //ScreenClear:::::::::::::::::::::::::::::::::::::
        clear();




        //Count of Chances
        chances=chances-1;
        cout<<"!!System UI!!: \n There are ";
        cout<<chances;
        cout<<" files that are to be permanently deleted.";





        //Retry Offer
        cout<< "\n Which directory ID *1* - *10* would you like to call? \n";
        cin>>a1;





        //ScreenClear:::::::::::::::::::::::::::::::::::::
        clear();





      }
    }


    //Cipher Arena entering
    cout<<"\aSystem UI: All Directories Destroyed!\n";
    sleep (2);
    cout<<"You will be taken back to the Chemical Laboratory Database Login shortly.\n";
  




    //ScreenClear:::::::::::::::::::::::::::::::::::::::
    sleep(2);
    clear();





    //RNG Game Checkpoint
    cout<<"Welcome to the Chemical Laborotary Database.\n";
    sleep (2);
    cout<<"Please Enter Your Key\n";
    cin>>cc;





    //Processing the RNG Checkpoint Key
    if (cc!="cobalt"){

      //RNG Checkpoint Key Invalid
      cout<<"The Key you have entered is incorrect. \n";
      sleep (3);
      clear ();

      type_text("\aENDING 1 : (Fail) LABORATORY KEY PERMANENTLY DELETED \n \a");
      sleep (2);
      clear ();
      sleep (2);
      clear ();
      
      type_text("\aHumanity is completely dependant upon you ");
      type_text("\aDo you choose to continue? (yes/no)");
      cin>>cont;
      if (cont=="no"){
        type_text("\aAnd thus, the most intelligent species on this planet perished, and the Universe continued on without them.");
        type_text_slow("It is The End.");
        sleep (2);
        clear ();
        cout<<"\aThanks for playing Cobalt Enigma!\n";
        game=1;
      }


    }
    else{

      //RNG Checkpoint Key Valid




    
      //Information on ciphers
      cout<<"\aYour information data has been cleared.\n There is one file remaining, consisting of elements.\n It has been marked as important.\n Decrypt it in accordance to the information supplied.\n";
      sleep (8);
      clear();
    
    
    
    
    
      //Translation
      cout<<"The Roots to our Most Recognised Language lies within this Ancient Tongue.\n";
      sleep (3);
      cout<<"Encryption: Argentum \n";

      cin>>trans_input;

      if (trans_input!=trans){

        cout<<"Decryption Failed.\n";
        sleep (2);
        cout<< "Move on \n";

      }
      else{








        //Post Translation
        clear ();
        cout<<"\aSystem Ui: IDENIFIED JOURNAL (.jnrl) FILE\n";
        sleep (3);
        cout<<"Opening file ... \n";
        clear();
        sleep (3);
        type_text_fast ("It is late at night when I am writing this.\n The neuro-virus, The Enigma,  has started to spread in exponential amounts across the globe.\n Today I have studied its general effects.\n The results have alarmed me.\n Many symptoms include pontentially permanent memory loss and extreme weakness.\n As I am writing this, many more thousands globally are getting affected.\n So far, all the treatments we have tried have worked to no avail.\n Hospitals and medical wards around the world are getting flooded with occupants.\n What is this enigmatic virus, and where did it come from?\n");
        cout<<"Decryption Successful. Note it down.\n";
        sleep(3);
        clear();

        //Ceasar
        cout<<"The Cryptography practiced by the Roman King, killed with the stabs of his peers, 23 times. It is used to a setting of Positive 3. \n";
        sleep (3);
        cout<<"Encryption: lrglqh \n";

        cin>>caesar_input;



        if (caesar_input!=caesar){

          cout<<"Decryption Failed.\n";
          sleep (2);
          cout<< "Move on \n";

          }
        else{
      
          //Post Caesar
          clear ();
          cout<<"\aSystem Ui: IDENIFIED JOURNAL (.jnrl) FILE\n";
          sleep (3);
          cout<<"Opening file ... \n";
          clear();
          sleep (3);
          type_text_fast ("I just finished my shift at the laboratory.\n I have been working on some Antidotes in the quarantine zone.\n We have made some discoveries on cell deconstruction and have developed an incubation chamber that can house a single person.\n The chamber can release particles constantly so as to preserve a body during its recovery.\n It cannot cure the virus.\n However, it can numb the effects of the Enigma. We only have a few at the laboratory which is good as all the prolonged exposure to the virus during research is sure to infect someone.\n");
          cout<<"Decryption Successful. Note it down.";
          sleep(3);
          clear();

          //Morse
          cout<<"Popularised in the 1830, this was based purely on binary. It was used to transmit messages over distances (especially on ships), but can only by transmitted letter by letter.\n";
          sleep(3);
          cout<<"Encryption: - .- -. - .- .-.. ..- -- \n";
        
          cin>>morse_input;
        


          if (morse_input!=morse){

            cout<<"Decryption Failed.\n";
            sleep (2);
            cout<< "Move on \n";
        
          }
          else{
        
        
            //post morse
            clear ();
            cout<<"\aSystem Ui: IDENIFIED JOURNAL (.jnrl) FILE\n";
            sleep (3);
            cout<<"Opening file ... \n";
            sleep (3);
            clear();
            type_text_fast ("Shift just ended. We ended later today as we have just gotten a lot more people to be treated\n. We also made an apparent discovery, that people who have been under the effects of this virus have fallen into a coma and memory loss seems to be a symtom.\n This is not good for us.\n The incubation pods could preserve bodies in stasis, but it would be impossible to create so many in a short time period.\n If only there was a solution.\n");
            cout<<"Decryption Successful. Note it down.";
            sleep(3);
            clear();
        
            //A1Z26 
            cout<<"This encryption method is very simple. Assign a number to a letter starting from A1 to Z26. Hence the name. \n";
            sleep (3);
            cout<<"Encryption: 20-9-20-1-14-9-21-13 \n";
          
            cin>>nual_input;
          


            if (nual_input!=nual){
            
              cout<<"Decryption Failed.\n";
              sleep (2);
              cout<< "Move on \n";
            
              }
            else{

              //Post A1Z26 
              clear ();
              cout<<"\aSystem Ui: IDENIFIED JOURNAL (.jnrl) FILE\n";
              sleep (3);
              cout<<"Opening file ... \n";
              sleep (3);
              clear();
              type_text_fast ("I just got sick.\n My temperature has risen to around 42 degrees celsius.\n This is not normal.\n I could not move today, and I feel weak.\n I did not really do much today.\n I just took rest.\n I called my co-worker Jack today.\n He told me that no other discoveries were made.\n I felt better at around 4, and reported to work for a while.\n I did some research and discovered something peculiar.\n Certain elements reacted to the infected cells differently.\n I will go and research more on this tomorrow.\n Most of my colleagues got infected yesterday, and have been put in their respective crytosis chambers.\n We need to come up with something swiftly or this could be the end.\n");


              cout<<"Decryption Successful. Note it   down.";
              sleep(3);
              clear();
            
              //Nato 
              cout<<"The North Atlantic Treaty Organization created this on 1 March 1956 so as to be used for effective radio communication. It is not just any Phoenetic Alphabet. \n";
              sleep(3);
              cout<<"Encryption: Oscar X-ray Yankee Golf Echo November \n";
            
              cin>>nato_input;
            


              if (nato_input!=nato){
              
                cout<<"Decryption Failed.\n";
                sleep (2);
                cout<< "Move on \n";
              
                }
              else{
            
                //Post Nato
                clear ();
                cout<<"System Ui: IDENIFIED JOURNAL (.jnrl) FILE\n";
                sleep (3);
                cout<<"Opening file ...\n ";
                sleep (3);
                clear();
                type_text_fast ("\aThe day has finally come.\n I am writing this in pure shock.\n All my colleagues are now unwell.\n  I looked at some of our experimental set-ups, and have located several of the previously mentioned elements.\n This diary that I am writing will serve to restore my memory on these events after I climb into my stasis chamber.\n I helped some of my colleagues into their chambers, and I looked through some papers.\n With this knowledge, I formulated a chemical equation.\n This could mean the life or death of our species.\n I do not think I will be strong enough to create this compound.\n I need to go into stasis quick.\n` This is my last message to the world.\n If I or anyone else ever finds this in the future, I would just like to say that the existence of mankind is in your hands.\n");
            
                cout<<"Decryption Successful. Note it down.";
                sleep(3);
                clear();
              
                //Passcode
                cout<<"Passcode \n";
                cout<<"This is to make sure that no-one other than the scientist can access this. This is essentially a protective measure. What is the password to this computer system? Only the scientist would rememeber, as he enters it whenever he logs on to his computer. \n";
              
                cin>> passcodenew;
              


                if (passcodenew!=password){
                
                  cout<<"The Passcode is Incorrect.";
                  clear ();
              
                }
                else{
              

                  //post passcode
                  cout<<"\a You have successfully passed authentication. That is because only the scientist would know this information. You are the scientist.";
                  clear();
                  cout<<"The final element is Nitrogen. \n";
            
                }
              }
            }
          }
      }
    }


    cout<<"What is the final Chemical Formula? (In order)";

    cin>>cf;

    if (cf != "AgITaTiON"){
    
      sleep(2);
      clear();
      type_text("ENDING 2: (Fail) UNDECIPHERABLE ENCRYPTION \n");
      sleep (2);
      clear ();
      type_text("Humanity is completely dependant upon you");
      type_text("Do you choose to continue? (yes/no)");
      cin>>cont;
      if (cont=="no"){
        type_text("And thus, the most intelligent species on this planet perished, and the Universe continued on without them.");
        type_text_slow("It is The End.");
        sleep (2);
        clear ();
        cout<<"\aThanks for playing Cobalt Enigma!\n";
        game=1;
      }
      sleep(2);
      cout<<"\aThanks for playing Cobalt Enigma!";
  
    }
    else{
    
      cout<<"AgITaTiON\n\n\n";

      sleep (3);
      type_text_fast("You sit back, eyes tearing up from the strain. You look up to the dim lights of the room, confusion and messy thoughts flowing everywhere in your mind.  You stagger over to the chemical lab table. There is a huge assortment of elements in containers in the wall. Many doubts plague your mind. Did the elements have to be at a certain state? Was there an order to it? There was no time to care about the specific details. You grappled at the containers. The chemical chamber of silver caught your eye. The letters Ar seemed to be calling out to you. Your breathing is shallow, due to the unfriendly environment. In a matter of minutes, you have grabbed all the elements and ripped them out of the capsules. You put a small sample of each in a test-tube. Sparks light up and electrical pulses dance through the tube. You grasp it with frail fingers and put it in a chemical centrifuge. You watch its perform its hypnotic swirl that adds to your throbbing headache. You pull out the tube, which now glowed a lucid bright blue. It reminded you of something special. Of something always there when you were growing up. The great magnificent void above everyones heads. Was it the sky? You snap back to reality. You bring the tube to your lips. The liquid flows down your throat. Strength spreads through your being. Your mind thinks of so many possibilities. Your spirit soars. Maybe, just maybe there is a happy ending.\n");
      type_text("ENDING 3: (Completion) Saviours of humanity \n\a");
      sleep(2);  
      cout<<"\aThanks for playing Cobalt Enigma!";
      return 0;
  
      }
    }




  }  
}