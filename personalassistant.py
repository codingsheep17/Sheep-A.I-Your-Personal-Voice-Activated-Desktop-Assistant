#Welcome to my personal desktop assistant (Jarvis A.I)

#Importing all of the important modules
import pyttsx3
import speech_recognition 
import webbrowser
import os
import requests
import datetime

class JarivsAi:

    def run(self):
        self.initializing_funcs()

    def initializing_funcs(self):
        self.speak_engine = pyttsx3.init() #initialized the speaking engine (i.e; jarvis)
        self.speak_engine.setProperty("rate", 135)
        self.recognizer = speech_recognition.Recognizer() #initializing the listening engine
        self.api_key = "d0255fcb16ffba5e824243e352a2d923"
        self.user_voice_command()

    def speak_only(self, voice_command_by_user):
        self.voice_command_by_user_speak = voice_command_by_user
        self.speak_engine.say(self.voice_command_by_user_speak)
        self.speak_engine.runAndWait()
    
    def speak_and_write(self, voice_command_by_user):
        try:
            self.speak_write = voice_command_by_user
            print(self.speak_write)
            self.speak_engine.say(self.speak_write)
            self.speak_engine.runAndWait()
        except Exception as sp_wr_error:
            print(f"Error {sp_wr_error}")
    
    def user_voice_command(self):
        self.running = True
        while self.running:
            self.speak_and_write("Say One Of The Following Option")
            print("""
1: Open Site
2: Open App
3: Provide Information
4: Date and Time
5: Temperature
6: Exit
""")
            """
            USER IS GIVING COMMAND AND THE INPUT COMMAND FOR THE MENU IS BEING PROCESSED IN THIS METHOD
            IF THE COMMAND ISN'T RECEIVED, TWO TYPE OF ERRORS WILL BE THROWN ON THE USER FACE, CAUSE HE'LL
            BE TOO MUCH DUMB TO UNDERSTAND THE SIMPLEST MENU EVER MADE IN THE AGES.
            """
            try:
                with speech_recognition.Microphone() as self.source:
                    print("Listening...")
                    self.audio = self.recognizer.listen(self.source)
                    try:
                        self.voice_command_by_user = self.recognizer.recognize_google(self.audio)
                        self.jarvis_responding()
                    except speech_recognition.UnknownValueError:
                        print("Sorry, I couldn't understand you.")
                    except speech_recognition.RequestError:
                        print("Server Issue or No Internet.")         
            except Exception as voice_cmd_error:
                print(f"Error {voice_cmd_error}")

    def jarvis_responding(self):
        #condition handling
        if self.voice_command_by_user.lower() == "open site":
            self.jarvis_opening_sites()
        elif self.voice_command_by_user.lower() == "open app":
            self.jarvis_opening_desktop_app()
        elif self.voice_command_by_user.lower() == "provide information":
            self.jarivs_giving_ai_info()
        elif self.voice_command_by_user.lower() == "date and time":
            self.jarvis_telling_datetime()
        elif self.voice_command_by_user.lower() == "temperature":
            self.ip_api()
        elif self.voice_command_by_user.lower() == "exit":
            self.speak_only("Thanks For Using Me, Bye!")
            self.running = False
        else:
            print("Kindly Speak Only One Option Given Above")

    def listen(self, prompt="Listening..."):
        self.speak_and_write(prompt)
        try:
            recognizer = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                audio = recognizer.listen(source)
                return recognizer.recognize_google(audio).lower().replace(" ", "")
        except speech_recognition.UnknownValueError:
                self.speak_and_write("Didn't catch that. Try again.")
                return None
        except speech_recognition.RequestError:
                self.speak_and_write("Server is down or no internet.")
                return None
        except Exception as listen_error:
            print(f"Error {listen_error}")
            return None



    def jarvis_opening_sites(self):
        print("""
1: Linkedin
2: Youtube
3: Instagram
4: Github
5: Solo Learn
""")
        self.user_site_command = self.listen("Listening Site...")
        self.sites_list = {
                "linkedin": "https://www.linkedin.com/in/syedhaseebshah19/",
                "youtube": "https://www.youtube.com/",  # update paths
                "instagram": "https://www.instagram.com/hxseeb._19/",
                "sololearn": "https://www.sololearn.com/en/profile/34572369",
                "github": "https://github.com/codingsheep17"
            }
        if self.user_site_command in self.sites_list:
            webbrowser.open(self.sites_list[self.user_site_command])
        else:
            self.speak_and_write("Sorry, Site Doesn't Exists")

    # todo: YOU CAN ADD MORE APPS FROM YOUR DEVICE BY REMOVING MINE
    def jarvis_opening_desktop_app(self):
            print("""
1: Notepad
2: Minecraft
3: Capcut
4: Need For Speed Most Wanted""")
            self.user_desktop_command = self.listen("Say the app name:")
            print(f"[DEBUG] Heard: {self.user_desktop_command}")
            self.desktop_apps_list = {
                "notepad": "notepad",
                "minecraft": r"C:\Users\haseeb\AppData\Roaming\.minecraft\minecraft.exe",  # update paths
                "capcut": r"C:\Users\haseeb\AppData\Local\CapCut\Apps\capcut.exe",
                "needforspeed": r"C:\Users\haseeb\Desktop\Games\Need-for-Speed-Most-Wanted-2005_www.FreeGamesDL.net\needforspeed.exe"
            }
            if self.user_desktop_command in self.desktop_apps_list:
                os.startfile(self.desktop_apps_list[self.user_desktop_command])
            else:
                self.speak_and_write("Sorry, App you said Doesn't Exist On Your Desktop")

    
    def jarvis_telling_datetime(self):
        self.today = datetime.datetime.today()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        month_matching = {
            1: "January",
            2: "February",  
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        self.month_to_show = month_matching[self.month]
        self.speak_and_write(f"Current Date Is {self.day}-{self.month_to_show}-{self.year}")
        #time
        self.current_datetime = datetime.datetime.now()
        self.formatted_time = self.current_datetime.strftime("%H Bajj Kay %M Minutes")
        self.speak_and_write(self.formatted_time)


    def ip_api(self):
         try:
              response = requests.get("http://ip-api.com/json/")
              location_data = response.json()
              self.lat = location_data["lat"]
              self.lon = location_data["lon"]
              self.city_name = location_data["city"]
              self.state_code = location_data["regionName"]  # optional if you still want
              self.api_setting()
         except Exception:
              self.speak_and_write("❌ Error while detecting location from IP.")

    def api_setting(self):
        try:
            self.weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric"
            self.data_fetching = requests.get(self.weather_api_url)
            self.data = self.data_fetching.json()
            self.show_weather_info()
        except Exception:
             self.speak_and_write(""" An Error Occured, Possibilites Are
1: Check Wether All Info is Added Correctly
2: Check Your Internet Connection
3: Check If the Server Site Is Responding or Not""")
    
    def show_weather_info(self):
         self.temp_celcius = 0.0
         self.temp_farenheit = 0.0
         self.speak_and_write(f"Weather Report for {self.city_name}, {self.state_code}")
         self.temp_celcius = self.data["main"]["temp"]
         self.temp_farenheit = (self.temp_celcius * 9/5) + 32
         
         self.jarvis_showing_temp()
    
             
    def jarvis_showing_temp(self):
        self.speak_and_write(f"Temperature is {self.temp_celcius:.1f} Centigrade & {self.temp_farenheit:.1f} farenheit")
         
        self.feels_like_temp = self.data["main"]["feels_like"]
        self.speak_and_write(f"Feels Like {self.feels_like_temp:.1f} Centigrade")
         
        if self.temp_celcius >= 45:
            self.speak_and_write("Extremely Hot (Stay hydrated)")    
        elif self.temp_celcius > 35 and self.temp_celcius < 44.9:
            self.speak_and_write("Very Hot (Limit outdoor activity)")    
        elif self.temp_celcius > 30 and self.temp_celcius < 34.9:
            self.speak_and_write("Hot (Sunblock recommended)")      
        elif self.temp_celcius > 25 and self.temp_celcius < 29.9:
            self.speak_and_write("Warm (Pleasant but sunny)")     
        elif self.temp_celcius > 15 and self.temp_celcius < 24.9:
            self.speak_and_write("Mild (Comfortable weather)")       
        elif self.temp_celcius > 5 and self.temp_celcius < 14.9:
            self.speak_and_write("Cool (Light jacket weather)")  
        elif self.temp_celcius > 0 and self.temp_celcius < 4.9:
            self.speak_and_write("Cold (Bundle up)")  
        elif self.temp_celcius > -10 and self.temp_celcius < -0.1:
            self.speak_and_write("Very Cold (Limit exposure)")  
        elif self.temp_celcius < -10:
            self.speak_and_write("Freezing (Dangerously cold)")     


    def jarivs_giving_ai_info(self):
        #AS I'M A STUDENT AND CAN'T AFFORD OPENAI API SO IM USING OPENROUTER WHICH IS FREE BUT NOT EFFICIENT
        self.speak_and_write("Give Your Command To Get Information")
        try:
            with speech_recognition.Microphone() as self.ai_command_source:
                print("Listening...")
                self.audio = self.recognizer.listen(self.ai_command_source)
                try:
                    self.ai_command_by_user = self.recognizer.recognize_google(self.audio)
                except speech_recognition.UnknownValueError:
                    print("Sorry, I couldn't understand you.")
                except speech_recognition.RequestError:
                    print("Server Issue or No Internet.")         
        except Exception as ai_cmd_error:
                print(f"Error {ai_cmd_error}")

        self.api_key = "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"
        self.url = "https://openrouter.ai/api/v1/chat/completions"
    
        self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        # api response processiing 
        # (user) can be replaced with the name of yours 
        self.data = {
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": f"{self.ai_command_by_user}"}]
            }
        
        self.res = requests.post(self.url, headers=self.headers, json=self.data)
        self.res_json = self.res.json()

        if "choices" in self.res_json:
            self.command = self.res_json["choices"][0]["message"]["content"]
        else:
            print("❌ API Error:", self.res_json)

       # ai response 
        print("Jarvis Giving Info...")
        self.speak_only(self.command)

jarvis_ai = JarivsAi()
jarvis_ai.run()