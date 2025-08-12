from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import pandas as pd


"""
    Note: The word "inmate" is not approved language, and is regarded as a slur by organizations like the Prison Policy Initiative. 
        I am using it in this code for the sake of matching the website's terminology.
"""

def get_top_level_links(driver):
    """
    This function gets all of the top level links from the main page.
    """
    # get all of the links
    # xpath selector is //*[@id="col0"]/a[1]
    links = driver.find_elements(By.XPATH, '//*[starts-with(@id, "col")]/descendant::a')
    link_hrefs = [link.get_attribute("href") for link in links]

    return link_hrefs

def process_links_list(driver, links):
    """
    This function processes a list of links and returns a list of processed links, since there are different types of facilities.
    """
    # Initialize a list to store processed links
    processed_links = []

    while links:
        url = links.pop(0)  # Get the first link

        if "institutions" in url:
            # If it's an institution link, add to processed list
            print(f"Processing institution link: {url}")
            processed_links.append(url)

        elif "search" in url:
            # If it's a search link, extract sublinks from the results
            print(f"Processing search link: {url}")
            driver.get(url)  # Navigate to the page
            try:
                # Wait for the results container to appear
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "all_results"))
                )

                # Locate the results container
                results_container = driver.find_element(By.ID, "all_results")

                # Find all facility links within the results container
                facility_links = results_container.find_elements(By.CSS_SELECTOR, "a.link-style2")

                # Extract sublinks and add them to the processed links list
                for link in facility_links:
                    sublink = link.get_attribute("href")
                    print(f"Found facility link: {sublink}")
                    processed_links.append(sublink)

            except Exception as e:
                print(f"Error processing search page {url}: {e}")

    return processed_links

def get_page_data(driver, link):
    """
    This function gets the data from a single page.
    """
    driver.get(link)  # Navigate to the page
    try:
        # Wait for the results container to appear
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "contact_email")))  # Locator for the email element

        # Initialize the elements dictionary
        elements = {}

        # Add name and description
        elements["name"] = driver.find_element(By.CLASS_NAME, "facl-title").text
        elements["description"] = driver.find_element(By.XPATH, '//div[@id="title_cont"]/p').text

        # Top-level information
        element_ids = ["address", "address2", "city", "state", "zip_code", "email", "phone", "county", "region"]

        # Add top-level information to the elements dictionary
        for element_id in element_ids:
            try:
                elements[element_id] = driver.find_element(By.XPATH, f'//*[@id="{element_id}"]').text
            except Exception:
                elements[element_id] = "missing"  # Handle missing elements gracefully

        judicial_district = driver.find_element(By.XPATH, '//td[text()="Judicial District:"]/following-sibling::td').text
        elements['judicial_district'] = judicial_district


        ## Inmate Resources Section:
        # Locate the 'inmate_resources' container
        resources_container = driver.find_element(By.ID, "inmate_resources")

        # Find all individual resource sections
        resource_sections = resources_container.find_elements(By.CLASS_NAME, "resource")

        # Dictionary to store section names and links
        inmate_resources = {}

        # Loop through each resource section
        for section in resource_sections:
            # Get the section name from the <h4> tag
            section_name = section.find_element(By.TAG_NAME, "h4").text

            # Find all <a> tags within this section and get their hrefs and texts
            links = section.find_elements(By.TAG_NAME, "a")
            section_links = {link.text.strip(): link.get_attribute("href") for link in links}

            # Store in the dictionary
            inmate_resources[section_name] = section_links

        elements["inmate_resources"] = inmate_resources

    except Exception as e:
                print(f"Error processing search page {link}: {e}")

    return elements

def get_machine_type():
    import platform
    return platform.machine()

def main():
    # get driver
    driver = webdriver.Chrome()

    # open main page
    driver.get("https://www.bop.gov/locations/list.jsp")

    # get top level links
    top_level_links = get_top_level_links(driver)

    # process the links
    processed_links = process_links_list(driver, top_level_links)

    page_data_list = []
    for link in processed_links[:5]:
        page_data = get_page_data(driver, link)
        page_data_list.append(page_data)

    # Append to df
    df = pd.DataFrame(page_data_list) 

    # write out
    df.to_csv("data/correctional_facilities.csv")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
