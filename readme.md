## Maximo DB Interface

In this documentation lets explore about the following.

- How to run the application locally
- How to create Docker image
- How to deploy the Docker image in the Code Engine (to access the app remotely)
- Creating Open API using Swagger
- Create Custom Extension in Watson Assistant
- Add Custom Extension to Watson Assistant

## 1. Run Locally

To run the application locally follow the below steps. 

<details><summary>CLICK ME</summary>

### 1.1 Download the repo

1. Download this repo 

2. Goto to the root folder of the repo.

3. Do the following steps. 

### 1.2 Env file

1. Create `.env` file with the below entries. 

2. Update all the properties accordingly.

```
LOGLEVEL=INFO

GENAI_API="https://us-xxxxxx.ibm.com/ml/v1/text/generation?version=2023-05-29"
### IBMCloud API Key
GENAI_KEY="xxxxxxx"
GENAI_PROJECT_ID="1c915286-xxxxxxfa4e"

MAXIMO_ATTRRIBUTE_URL="https://xxxxxx.com/maximo/api/os/MXAPIMAXATTRIBUTE?oslc.where=persistent=1%20and%20objectname=%22"
MAXIMO_RUNSQL_URL="https://xxxxxxxxxxxx.com/maximo/api/script/runsql?lean=1&ignorecollectionref=1"
MAXIMO_API_KEY="xxxxxxxxxxxxx"
```

### 1.3  Run the app

1. Runs the below command to start the app

```
python main.py
```

2. Open the below urls in a browser to verify the app is running.

http://localhost:8080/hello/

http://localhost:8080/books/

http://localhost:8080/maximo/


3. Run the below curl script to test the maximo api.

```
curl -X 'POST' \
  'http://localhost:8080/maximo/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "What is the worktype of workorder 1309?"
}'
```

It would give the output like the below.
```
{
  "result": [
    {
      "WORKTYPE": "PM"
    }
  ]
}
```
</details>

## 2. Create Docker Image

You can create docker images using podman and run the app in the code engine.

Here docker.io is used as a image repository. You can use as per your wish.

In the below example we used `gandigit` as a docker id. You have to change it to your docker id.

<details><summary>CLICK ME</summary>

#### 2.1 Docker login

1. Run the below command to login into docker.io

```
podman login -u gandigit docker.io
```

#### 2.2 Create Image

1. Run the below command to create docker image

```
podman build --platform linux/amd64 -f Dockerfile -t docker.io/gandigit/maixmo-db-interface:latest .
```

#### 2.3 Push image to the Image Repository

1. Run the below command to push the created image to the repository

```
podman push docker.io/gandigit/maixmo-db-interface:latest
```

</details>

## 3. Deploying the Docker Image in Code Engine

Lets deploy the created docker image in the Code Engine.


<details><summary>CLICK ME</summary>

#### 3.1 Create Project

1. In Projects screen, click on `Create` button

<img src="images/image11.png">

2. Choose `Location` as per your need.

3. Enter any Project `Name `

4. Click on `Create` button

<img src="images/image12.png">

Project is created.

5. Click on the created project

<img src="images/image13.png">

#### 3.2. Create Application

1. In Application screen, click on `Create` button

<img src="images/image14.png">

2. Enter any Application `Name`

3. Enter the `Docker Image name` that we already created.

4. Click on `Configure image` button

<img src="images/image15.png">

5. Choose `https://index.docker.io/v1/` in the `Registry server` drop down list.

The rest of the details would be auto filled based on the docker image name that we entered in the previous screen.

6. Click on `Done` button in the image configuration screen.

<img src="images/image16.png">

7. Click on `Create` button

<img src="images/image17.png">

8. Application got created.

<img src="images/image18.png">


#### 3.3. Create Environment variable

1. Click on the application name from the above screen.

The application page get displayed.

2. Click on `Configuration` tab. 

<img src="images/image19.png">

3. Click on `Environment Variables` tab. 

4. Click on `Add environment variable` menu. 

<img src="images/image20.png">

5. Choose `Literal value` Option.

6. Enter `Environment variable name` and `Value` columns values.

7. Click on `Add` Option.

<img src="images/image21.png">

8. Click on `Add` Option. The variable got created.

9. Similarly create an entry for each Environment variables mentioned in the `.env-sample` file.

<img src="images/image22.png">

10. Click on `Deploy` Option to redeploy the app with the created environment variables.

<img src="images/image23.png">

#### 3.4. Open the Application

1. In the application screen, Click on the `Open URL` link to open the application. 

<img src="images/image24.png">

</details>


## 4. Creating Open API using Swagger

Lets create open API using swagger. This open api json is needed to create extension in Watson Assistant for WA and this app integration.


<details><summary>CLICK ME</summary>

#### Create Open API 

1. Open the URL https://converter.swagger.io/ in your browser

2. In the `GET / Convertor` method, click on the `Try it out` button

3. In the `URL` text box enter the App url suffixed with `swagger.json`

    Ex:     https://maxxxxxxxx.appdomain.cloud/swagger.json

<img src="images/image50.png">


4. Click on `Execute` button

The Open API json should have got created. 

<img src="images/image51.png">

5. Click on `Download` button

6. Open the downloaded json and update the App url as highlighted 

<img src="images/image52.png">

</details>

## 5. Create Custom Extension in Watson Assistant

Lets create Custom Extension in Watson Assistant to call the app.

<details><summary>CLICK ME</summary>


1. In Watson Assistant, Click on `Extension` button

<img src="images/image53.png">

2. Click on `Build custom extension` button
<img src="images/image54.png">

3. Click on `Next` button
<img src="images/image55.png">

4. Enter any Name for the extension.
<img src="images/image56.png">

5. Click on `Drag and drop file here or click to upload` link
<img src="images/image57.png">

6. Choose the Open API Json that was generated in the previous section.

7. Click on `Next` button
<img src="images/image58.png">

8. See the list of APIs imported.

9. Click on `Finish` button
<img src="images/image59.png">

Extension got created.
<img src="images/image60.png">



</details>

## 6. Add Custom Extension to Watson Assistant

Once the Custom Extension is created, it has to be added to WA.

<details><summary>CLICK ME</summary>

1. In the created Extension, Click on `Add` button

<img src="images/image60.png">

2. Click on `Add` button
<img src="images/image61.png">

3. Click on `Next` button
<img src="images/image62.png">

4. Click on `Next` button
<img src="images/image63.png">

5. Click on `Finish` button
<img src="images/image64.png">

Extension got added.
<img src="images/image65.png">

</details>
