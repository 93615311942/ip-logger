try:
    from flask import Flask
    from flask import request
    from datetime import datetime
    from flask import render_template

except ImportError as Ie:
    print(f"[ ! ] Missing dependency '{Ie}'")

class IpLogger():
    """
        Class to handle the IpLogging

        Args:
            None
        
        Returns:
            None
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.log_file = 'log.txt'
        self._register_routes()

    def get_info_of_visitor(self) -> str:
        """
            Function get parse the vistor information from the request.

            Args:
                None

            Returns:
                None
        """
        visitor_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        referrer = request.headers.get('Referer', 'No Referrer')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        visitor_info = f"[{timestamp}] IP: {visitor_ip}, User-Agent: {user_agent}, Referrer: {referrer}\n"
        
        return visitor_info
    
    def log_data(self,visitor_data: str) -> None:
        """
            Helper function to log the visiter data into 'log.txt'.

            Args:
                visitor_data    (str): Vister data like ip ,user agent to log.
            
            Returns:
                None
        """
        try:
            with open(self.log_file , "a") as log_file:
                log_file.write(visitor_data)
            
            return None
        
        except Exception as Ue:
            print(f"[ ! ] Unexpected exception : {Ue}")

    def _register_routes(self) -> str:
        """
            Function to register the routes for flask.

            Args:
                None

            Returns:
                None
        """
        @self.app.route("/",methods = ['GET'])
        def index():
            """
                Sub function for the / of the app.

                Args:
                    None

                Returns:
                    None
            """
            try:
                visiter_info = self.get_info_of_visitor()
                self.log_data(visiter_info)
                return render_template('index.html')
            
            except Exception as Ue:
                print(f"[ ! ] Unexpected exception : {Ue}")

    def main(self):
        """
            Main Function for the ip logger.

            Args:
                None
            
            Returns:
                None
        """
        self.app.run(host='0.0.0.0',port=5000)

if __name__ == '__main__':
    ip_logger = IpLogger()
    ip_logger.main()