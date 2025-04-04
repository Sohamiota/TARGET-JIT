Below is a **README.md** file tailored to explain the Sales Prediction and Inventory Optimization Web Application project based on the provided code. It includes an overview, features, dependencies, setup instructions, usage guidelines, and additional details to help users understand and run the project.

---

# Sales Prediction and Inventory Optimization Web Application

## Project Overview

This web application, built with Streamlit, is designed to assist businesses—such as shopkeepers, retailers, and other business owners—in forecasting sales and optimizing inventory levels. It leverages machine learning models to predict future sales and provide inventory recommendations based on uploaded sales data. The application includes user authentication, data visualization, and interactive features to enhance usability.

### Features

- **User Authentication**: Secure signup, login, and password reset functionality with password hashing and SQLite-based user management.
- **Data Upload**: Upload up to 5 CSV or XLSX files containing sales data (must include 'Sales' and 'Date' columns).
- **Sales Prediction**: Forecast future sales using multiple models:
  - Linear Regression
  - Random Forest
  - ARIMA
  - LSTM (Long Short-Term Memory)
- **Inventory Optimization**: Calculate safety stock levels and reorder points using Random Forest and ARIMA models.
- **Default Datasets**: Preloaded datasets for holidays and customer information to enhance forecasting.
- **Interactive Dashboard**: Visualize predictions with Plotly charts and download forecast data as CSV files.
- **Feedback and Support**: Submit questions, provide feedback, and rate the app experience.
- **Responsive Design**: Supports light and dark mode with custom CSS styling.

## Dependencies

To run this application, you need to install the following Python packages. These are required for the machine learning models, data processing, web interface, and database management:

- **Streamlit**: For creating the web application interface.
- **Pandas**: For data manipulation and handling.
- **NumPy**: For numerical computations.
- **Scikit-learn**: For Linear Regression and Random Forest models.
- **TensorFlow**: For LSTM model implementation.
- **Statsmodels**: For ARIMA model implementation.
- **Plotly**: For interactive data visualizations.
- **Chardet**: For detecting file encodings during uploads.
- **SQLite3**: For storing user data (included with Python standard library).
- **Hashlib**: For password hashing (included with Python standard library).

Install the dependencies using the following command:

```bash
pip install streamlit pandas numpy scikit-learn tensorflow statsmodels plotly chardet
```

**Note**: Ensure you have Python 3.7 or higher installed, as some dependencies may not support earlier versions.

## Setup Instructions

Follow these steps to set up and run the application on your local machine:

1. **Clone the Repository**:
   - Clone this repository to your local machine:
     ```bash
     git clone <repository-url>
     ```
   - Replace `<repository-url>` with the actual URL of your repository.

2. **Install Dependencies**:
   - Navigate to the project directory:
     ```bash
     cd <project-directory>
     ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```
   - If a `requirements.txt` file is not provided, create one with the following content and then run the above command:
     ```
     streamlit
     pandas
     numpy
     scikit-learn
     tensorflow
     statsmodels
     plotly
     chardet
     ```

3. **Prepare Media Files**:
   - Ensure the following files are in the project directory (as referenced in the code):
     - `logo2.png`: Application logo.
     - `banner3.jpeg`: Banner image for the dashboard.
     - `icon2.png`: Page icon.
     - `an_animation_of_a_hand_drawn_business_strategy_with_chart_preview.mp4`: Video for the logout page.
   - If these files are missing, either replace them with your own or update the code to remove these references.

4. **Database Setup**:
   - The application uses SQLite to manage user data. A database file named `users_data.db` will be created automatically in the project directory upon first run.

5. **Run the Application**:
   - Start the Streamlit server:
     ```bash
     streamlit run app.py
     ```
   - The code assumes the main file is named `app.py`. Adjust the filename in the command if it differs.

6. **Access the Application**:
   - Open your web browser and navigate to:
     ```
     http://localhost:8501
     ```

## Usage

1. **Sign Up / Log In**:
   - **Sign Up**: Create a new account using a username or email and password.
   - **Log In**: Use existing credentials to access the dashboard.
   - **Reset Password**: Recover your account by resetting your password via username or email.

2. **Upload Sales Data**:
   - Upload up to 5 CSV or XLSX files with sales data. Each file must contain:
     - A 'Sales' column (or similar, e.g., 'Revenue', 'QuantitySold'; the app will attempt to detect it).
     - A 'Date' column (or similar, e.g., 'Order Date'; the app will identify it).
   - Preview your data after uploading.

3. **Sales Prediction**:
   - Select a forecasting model (Linear Regression, Random Forest, ARIMA, or LSTM) for each dataset.
   - Adjust forecast days (1–30) and view predictions.
   - Download forecast data as a CSV file.

4. **Inventory Optimization**:
   - Set a safety stock level (100–1000) via a slider.
   - Choose between Random Forest or ARIMA for inventory recommendations.
   - View calculated safety stock and reorder points.

5. **Explore Additional Features**:
   - **Default Datasets**: View and edit preloaded holiday and customer data.
   - **About**: Learn about the models and features.
   - **Ask a Question**: Submit inquiries for support.
   - **Feedback**: Rate the app and leave comments.
   - **Logout**: End your session securely.

## Project Structure

- **`app.py`**: Main application file containing the Streamlit code and logic.
- **`users_data.db`**: SQLite database file for user information (created automatically).
- **`logo2.png`, `banner3.jpeg`, `icon2.png`**: Media files for the interface.
- **`an_animation_of_a_hand_drawn_business_strategy_with_chart_preview.mp4`**: Logout page video.
- **`requirements.txt`**: List of dependencies (create manually if not provided).

## Notes

- **File Encoding**: The app uses `chardet` to detect CSV file encodings. If issues arise, it falls back to `ISO-8859-1`.
- **Large Datasets**: For datasets over 50 MB, the app suggests using advanced models like LSTM or XGBoost (not yet implemented).
- **Error Handling**: The app includes warnings for missing columns or invalid data formats.

## Future Improvements

- Add support for external factors like marketing campaigns in predictions.
- Implement advanced models such as XGBoost and Prophet.
- Enhance user management with profile editing and multi-user support.

---

This README provides a comprehensive guide to understanding, setting up, and using the Sales Prediction and Inventory Optimization Web Application. Customize the repository URL, file names, and media file references as needed for your specific setup.
