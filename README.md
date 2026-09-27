# da12-predictor
1. Create a GitHub Repository
 -Title,public,README.md,.gitignore:python
 -Clone the repo by copying the code(setting=local)
    - https://github.com/Khadijak2/da12-predictor.git 
    -In the appropriate folder, right click and select "open GitBash here"
    -Run the code link and open folder in VS Studio

2. Create a virtual environment
-python -m venv da12-predictor
-activate the env name\Scripts\Activate
-In case of error, execute this command: Set-ExecutionPolicy RemoteSigned -Scope, to get permission
-install the required libraries: pip install jupyter ipykernel numpy pandas matplotlib seaborn scikit-learn

3. Model Training on the required dataset (model.ipynb)
-select the kernel
-load data (salary dataset) and import libraries
-data cleaning, preprocessing,and train_test_split
-train the model(linear regression)
-evaluate the model using y_pred and y_test (r2, mae, mse, rmse)
-test the model on new YoE values to check model's accuracy
-Serialize the model using the pickle library

4. Creation of streamlit UI and uploading app.py to it (local testing)
-Run streamlit app by: streamlit run app.py 
-import libraries
-establish website title "DA-12 Predictor", suitable symbol, page titles and sub-titles
-load serilaized model
-define input fields: yoe=st.number_input('Years of Experience',min_value=0.0,max_value=10.0,step=0.5,value=2.0)
-Use other functions of streamlit cheat sheet to make interface attractive (button, slider, etc.)
-make salary/y value predictions: st.success

5. create requirements.txt
-mention libraries/modules with their respective versions by running code in model.ipynb file

6. Export files to GitHub
-Git add commit push to export the model.sp, model.ipynb,readme.md,app.py and .gitignore to github

7. Sign up on streamlit community cloud to allow access to other people
-connect and continue with GitHub
-select repository + app.py
-deploy and test the live application



    