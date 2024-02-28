<h1 align="center">API Chatbot PT SMI</h1>

## Table of Contents
1. [Information About App](#api-info)
2. [Our Main Feature](#main-feature)

   a. [Simple Chat Interface between User and System](#chat-frontend)

   b. [Chat with History](#chat-history)
   
3. [System's Flow](#systems-flow)
4. [Tech Stack](#tech-stack)
5. [How to Run Locally](#run-local)
6. [How to Deploy](#deploy)
7. [Live Instance](#live-instance)
8. [Related Repository](#related-repo)

<a name="api-info"></a>
## Information About this App
Tampilan website sederhana yang dibangun menggunakan framework Streamlit. Website ini merupakan tampilan atau frontend dari sistem ChatBot PT SMI yang sebelumnya sudah kami kembangkan. Website ini hanya menampilkan interaksi atau chat yang terjadi antara pengguna dengan sistem backend <a href='https://github.com/dutaramadhan/API-ChatBot-PT-SMI'>ChatBot PT SMI</a>. Website ini mampu menyimpan history chat di dalam array yang diberikan kepada API ChatBot sebagai input agar sistem memahami percakapan atau interaksi yang sebelumnya dilakukan oleh user dan juga sistem.
![Tampilan Website](https://drive.google.com/file/d/1CpvhGemfxAdzEMBwoMH9L0mPVsGm6TQl/view?usp=drive_link)

<a name="main-feature"></a>
## Main Features
<a name="chat-frontend"></a>
### a. Simple Chat Interface between User and System
Fitur untuk menampilkan interaksi atau percakapan pengguna dengan sistem. Bertujuan agar sistem lebih mudah untuk digunakan, dipahami, dan lebih menarik bagi pengguna.
<a name="chat-history"></a>
### b. Chat with History
Fitur untuk menyimpan data percakapan pengguna dan sistem ke dalam bentuk list yang nantinya dapat digunakan sebagai input bagi sistem agar sistem memahami percakapan atau interaksi yang sebelumnya dilakukan oleh user dan juga sistem.

<a name="systems-flow"></a>
## System's Flow

<a name="tech-stack"></a>
## Tech Stack
### 1. Python
### 2. Streamlit
### 4. Docker

<a name="run-local"></a>
## How to Run Locally
1. Clone repositori ini
   ```
   git clone https://github.com/dutaramadhan/API-ChatBot-PT-SMI.git
   ```
2. Ikuti cara set up dan run yang ada di dokumentasi
3. Clone repositori ini
   ```
   git clone https://github.com/ncgalih/Frontend-ChatBot-PT-SMI.git
   ```
4. Buka direktori Frontend-ChatBot-PT-SMI
5. Install pyhton virtual environtment 
   ```
   pip install virtualenv
   ```
6. Buat virtual environment
   ```
   virtualenv venv
   ```
7. Aktifkan virtual environment
   - Windows
     ```
     venv/Scripts/activate
     ```
   - Linux/macOS
     ```
     source venv/bin/activate
     ```
8. Install semua library atau depedensi yang dibutuhkan
   ```
   pip install -r requirements.txt
   ```
9. Buat file .env
   ```
   API_CHATBOT = ...
   ```
10. Jalankan aplikasi
    ```
    python -m streamlit run app.py --server.port <<port>> 
    ```
11. Cek apakah server sedang berjalan
    ```
    http://localhost:<<port>>/
    ```

<a name="deploy"></a>
## How to Deploy
1. Buat file .env
   ```
   API_CHATBOT = ...
   ```
2. Build docker image
   ```
   docker build -t frontend-chatbot .
   ```
3. Run docker image
   ```
   docker run -d -p 5003:5003 --name frontend-chatbot frontend-chatbot
   ```
4. Cek apakah server sedang berjalan
    ```
    http://<ip-host>:5003/
    ```

<a name="live-instance"></a>
## Live Instance
http://10.10.6.69:5003

<a name="related-repo"></a>
## Related Repository
- <a href='https://github.com/dutaramadhan/API-Query-Data-PT-SMI'>API-Query-Data-PT-SMI</a>
- <a href='https://github.com/dutaramadhan/API-Otomasi-ETL-PT-SMI'>API-Otomasi-ETL-PT-SMI</a>
- <a href='https://github.com/dutaramadhan/API-ChatBot-PT-SMI'> API-ChatBot-PT-SMI</a>
