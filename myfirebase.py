import requests
import json
from kivy.app import App


class MyFirebase():
    wak = "AIzaSyBLFxWiQynQj-BmkfxOaiXgjojNGLnGDrg"    #web API key
    def sign_up(self, email, password):
        app = App.get_running_app()
        #Send email and password to firebase
        #Firebase will return a localId , authToken , refreshToken
        signup_url="https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wak
        signup_payload = {"email":email,"password":password,"returnSecureToken": True}
        sign_up_request = requests.post(signup_url, data=signup_payload)
        print(sign_up_request.ok)
        print(sign_up_request.content.decode())
        sign_up_data = json.loads(sign_up_request.content.decode())


        if sign_up_request.ok == True:
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            idToken = sign_up_data['idToken']

            # Save refreshToken to a file
            with open("refresh_Token.txt", "w") as f:
                f.write(refresh_token)

            # Save localId to a variable in main app class
            # Save idToken to a variable in main app class

            app.local_id = localId
            app.id_token = idToken

            #get user id
            #get request on firebase to get the user
            user_get_req = requests.get("https://wazzup-1bca4-default-rtdb.firebaseio.com/next_user_id.json?auth=" + idToken)
        
            print("user",user_get_req.json())
            new_user_id = user_get_req.json()
            #update firebase's user id field
            #user_patch_data='{"new_user_id": %s}' % str(next_user_id+1)
            #user_patch_req=requests.patch("https://wazzup-1bca4-default-rtdb.firebaseio.com/.json?auth=" + idToken,data = user_patch_data)
            #Create new key in database from localId
            my_data='{"email": "" , "password" : "" , "new_user_id": ""}'
            post_request= requests.patch("https://wazzup-1bca4-default-rtdb.firebaseio.com/"+localId+".json?auth="+idToken,data=my_data)
            print(post_request.ok)
            print(json.loads(post_request.content.decode()))

            app.change_screen("home_screen")


        if sign_up_request.ok == False:
            error_data = json.loads(sign_up_request.content.decode())
            error_message =error_data['error']['message']
            app.root.ids['login_screen'].ids['login_message'].text = error_message
        pass


    def exchange_refresh_token(self, refresh_token):
        refresh_url = "https://securetoken.googleapis.com/v1/token?key=" + self.wak
        refresh_payload = '{"grant_type":"refresh_token" , "refresh_token":"%s"}'% refresh_token
        refresh_req=requests.post(refresh_url , data=refresh_payload)
        print("REFRESH IS OK honey?",refresh_req.ok)
        print(refresh_req.json())
        id_token = refresh_req.json()['id_token']
        local_id =refresh_req.json()['user_id']
        return id_token, local_id




