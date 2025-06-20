from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "R9ZY200Z80M"
options.automation_name = "UiAutomator2"
options.app_package = "com.eekifoods.dev"
options.app_activity = "com.eekifoods.MainActivity"
options.no_reset = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
wait = WebDriverWait(driver, 10)

time.sleep(3)

# Open Media Moisture section
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Media Moisture"]/android.widget.TextView').click()
time.sleep(1)

# Tap + icon
plus_icon_xpath = (
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
    'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
    'android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/'
    'android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/'
    'android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.Button/android.widget.TextView'
)
wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, plus_icon_xpath))).click()
time.sleep(1)

# Field XPaths
field_xpaths = {
    "dome": "/hierarchy/.../android.view.ViewGroup[1]/android.widget.EditText",
    "section": "/hierarchy/.../android.view.ViewGroup[2]/android.widget.EditText",
    "ec": "/hierarchy/.../android.view.ViewGroup[3]/android.widget.EditText",
    "moisture": "/hierarchy/.../android.view.ViewGroup[4]/android.widget.EditText",
    "temperature": "/hierarchy/.../android.view.ViewGroup[5]/android.widget.EditText"
}


xpath_prefix = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup"


def fill_field(xpath, value, label):
    try:
        field = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath)))
        field.click()
        time.sleep(0.3)
        field.clear()
        time.sleep(0.3)
        field.send_keys(value)
        print(f"✅ {label} entered: {value}")
    except Exception as e:
        print(f"❌ Failed to enter {label}: {e}")
        raise

# Loop for 50 entries
for i in range(50):
    print(f"\n📄 Filling record {i + 1}")

    try:
        fill_field(f"{xpath_prefix}/android.view.ViewGroup[1]/android.widget.EditText", f"Dome-{i+1}", "Dome")
        fill_field(f"{xpath_prefix}/android.view.ViewGroup[2]/android.widget.EditText", f"Section-{i+1}", "Section")
        fill_field(f"{xpath_prefix}/android.view.ViewGroup[3]/android.widget.EditText", f"{1.0 + i * 0.1:.1f}", "EC")
        fill_field(f"{xpath_prefix}/android.view.ViewGroup[4]/android.widget.EditText", f"{35.0 + i * 0.5:.1f}", "Moisture")
        fill_field(f"{xpath_prefix}/android.view.ViewGroup[5]/android.widget.EditText", f"{25.0 + i * 0.2:.1f}", "Temperature")

        if i == 49:
            # Submit only after last entry
            submit_btn = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]/android.widget.TextView')))
            submit_btn.click()
            print("🚀 Final record submitted.")

        time.sleep(1)

    except Exception as e:
        print(f"[ERROR] Record {i+1} failed: {e}")
        break

# Optionally close
# driver.quit()
