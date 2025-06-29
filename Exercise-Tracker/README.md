# 🏋️ Workout Tracker

A Python-based exercise tracking application that uses natural language processing to log workouts automatically to Google Sheets.

## 🎯 Overview

This application allows you to:
- Input exercises in natural language (e.g., "I ran 3 miles and did 20 pushups")
- Automatically calculate calories burned using the Nutritionix API
- Log workout data (date, time, exercise, duration, calories) to Google Sheets via Sheety API
- Run continuously in a loop for multiple workout entries

## 🚀 Features

- **Natural Language Processing**: Describe your workout in plain English
- **Automatic Calorie Calculation**: Based on your personal profile (age, weight, height, gender)
- **Google Sheets Integration**: Seamless logging to your personal workout spreadsheet
- **Continuous Operation**: Keep the app running for multiple workout entries
- **Error Handling**: Robust error management for API calls and user input

## 📋 Prerequisites

Before running this application, you'll need:

1. **Python 3.7+** installed on your system
2. **API Keys** from the following services:
   - [Nutritionix API](https://www.nutritionix.com/business/api) (App ID & API Key)
   - [Sheety API](https://sheety.co/) (Bearer Token & Endpoint URL)
3. **Google Sheet** set up for workout tracking

## 🛠️ Installation

### 1. Clone or Download the Code
```bash
git clone <your-repo-url>
cd workout-tracker
```

### 2. Install Required Packages
```bash
pip install requests python-dotenv
```

### 3. Set Up Environment Variables

Create an `env.txt` file in your project directory:

```env
ENV_NIX_APP_ID=your_nutritionix_app_id
ENV_NIX_API_KEY=your_nutritionix_api_key
ENV_SHEETY_ENDPOINT=your_sheety_endpoint_url
ENV_SHEETY_TOKEN=your_sheety_bearer_token
```

## ⚙️ Configuration

### Personal Profile Setup

Update the user profile constants in the code:

```python
GENDER = "male"        # "male" or "female"
WEIGHT_KG = 69         # Your weight in kilograms
HEIGHT_CM = 185        # Your height in centimeters  
AGE = 20              # Your age in years
```

### Google Sheet Setup

1. Create a Google Sheet with the following columns:
   - Date
   - Time
   - Exercise
   - Duration
   - Calories

2. Name your sheet "workout" (or update the `GOOGLE_SHEET_NAME` variable)

3. Connect your sheet to Sheety and get your API endpoint

## 🔧 Environment Setup Guide

### PyCharm Users

1. Go to **Run** → **Edit Configurations**
2. Find **Environment** → **Environment Variables**
3. Click the folder icon to open the environment variables window
4. Paste your environment variables in `KEY=VALUE` format

### Replit Users

1. Click the **padlock symbol (Secrets)** in the side menu
2. Add environment variables one by one, or
3. Upload a JSON file with your variables:
```json
{
  "ENV_NIX_APP_ID": "your_app_id",
  "ENV_NIX_API_KEY": "your_api_key",
  "ENV_SHEETY_ENDPOINT": "your_endpoint",
  "ENV_SHEETY_TOKEN": "your_token"
}
```

### Command Line Users

Create a `.env` file or export variables:
```bash
export ENV_NIX_APP_ID="your_app_id"
export ENV_NIX_API_KEY="your_api_key"
export ENV_SHEETY_ENDPOINT="your_endpoint" 
export ENV_SHEETY_TOKEN="your_token"
```

## 🚀 Usage

1. **Run the application:**
```bash
python workout_tracker.py
```

2. **Enter your workout:**
```
Tell me which exercises you did: I ran for 30 minutes and did 50 pushups
```

3. **Continue logging or exit:**
- Enter more exercises to continue
- Type `quit`, `exit`, or `q` to stop

## 🔍 API Integration Details

### Nutritionix API
- **Purpose**: Natural language exercise recognition and calorie calculation
- **Endpoint**: `https://trackapi.nutritionix.com/v2/natural/exercise`
- **Authentication**: App ID + API Key headers

### Sheety API  
- **Purpose**: Google Sheets integration
- **Authentication**: Bearer Token
- **Format**: JSON payload with workout data

## 🐛 Troubleshooting

### Common Issues

#### ❌ KeyError: Environment Variable Not Found
**Problem**: Python can't find your environment variables

**Solutions**:
- Verify variable names match exactly (case-sensitive)
- Check your `env.txt` file format
- Ensure no extra spaces around `=` signs
- Restart your IDE after adding environment variables

#### ❌ Sheety: Insufficient Permission  
**Problem**: Sheety can't access your Google Sheet

**Solutions**:
1. Sign out of Sheety and sign back in
2. Grant full permissions during sign-in
3. Check Google Account → Security → Third Party Apps
4. Verify Sheety is listed with proper permissions

#### ❌ Sheety: Bad Request - JSON Payload Error
**Problem**: Incorrect sheet naming or API structure

**Solutions**:
- Ensure Google Sheet name is plural (e.g., "workouts", not "workout")
- Use camelCase for sheet names with spaces (e.g., "myWorkouts")
- API dictionary key should be singular camelCase (e.g., "myWorkout")
- Refresh your Sheety API page after changes

#### ❌ Nutritionix API Errors
**Problem**: Exercise recognition or API call failures

**Solutions**:
- Verify your App ID and API Key are correct
- Check your input format (natural language works best)
- Ensure your personal profile data is accurate
- Try simpler exercise descriptions first

## 📊 Data Structure

### Workout Entry Format
```json
{
  "date": "29/06/2025",
  "time": "14:30:00", 
  "exercise": "Running",
  "duration": 30,
  "calories": 350
}
```

## 🔒 Security Notes

- Never commit your `env.txt` or `.env` files to version control
- Add these files to your `.gitignore`
- Keep your API keys secure and don't share them
- Regularly rotate your API keys if needed

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your API keys and permissions
3. Review the error messages for specific guidance
4. Open an issue in the project repository