<h1>Automated greenhouse.io Forms</h1>

<p align="center">
    <!-- code size  -->
    <img src="https://img.shields.io/github/languages/code-size/GSPuniani/automated-greenhouse-forms" />
    <!-- issues -->
    <img src="https://img.shields.io/github/issues/GSPuniani/automated-greenhouse-forms" />
    <!-- pull requests -->
    <img src="https://img.shields.io/github/issues-pr/GSPuniani/automated-greenhouse-forms" />
    <!-- number of commits per year -->
    <img src="https://img.shields.io/github/commit-activity/y/GSPuniani/automated-greenhouse-forms" />
    <!-- last commit -->
    <img src="https://img.shields.io/github/last-commit/GSPuniani/automated-greenhouse-forms" />
</p>


- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)


## Project Overview

Many job application forms are hosted on a subdomain of greenhouse.io. However, the process of filling out forms on greenhouse.io can be unnecessarily time-consuming and tedious. Job applicants must manually type out their personal information for each application. Unfortunately, it is not possible to save this information because applicants cannot create accounts on greenhouse.io (only recruiters can). 

This project is an attempt to automate the process of filling out these greenhouse.io forms. Instructions for downloading and running the Python script are included below.



## Requirements

| Platform | Minimum Swift Version | Installation | Status |
| --- | --- | --- | --- |
| iOS 10.0+ / macOS 10.12+ / tvOS 10.0+ / watchOS 3.0+ | 5.1 | [CocoaPods](#cocoapods), [Carthage](#carthage), [Swift Package Manager](#swift-package-manager), [Manual](#manually) | Fully Tested |
| Linux | Latest Only | [Swift Package Manager](#swift-package-manager) | Building But Unsupported |
| Windows | Latest Only | [Swift Package Manager](#swift-package-manager) | Building But Unsupported |


## Installation

### Customization

There are currently three options for your browser choice: Safari, Chrome, and Firefox. You can run the script as is if you want to use Firefox, since it is the default option. If you would prefer to use Safari or Chrome, follow the respective instructions below.

#### Safari

- Uncomment this line: `browser = webdriver.Safari()`. (Uncommenting a line means removing the hashtag and empty space from its immediate left.) 
- Comment out this line: `browser = webdriver.Firefox()`. (Commenting out a line means adding a hashtag to its immediate left.)
- Open a Safari window, click on the "Develop" in the menu bar at the top, and make sure that the option for "Allow Remote Automation" has a checkmark next to it. You can click on it to enable it if the check mark is absent.
    -  Note: If your menu bar does not have a "Develop" menu between "Bookmarks" and "Window", then you can enable it by clicking on the "Safari" menu, opening "Preferences", selecting the "Advanced" tab on the far-right, and then clicking the checkbox at the bottom to "Show Develop menu in menu bar".


#### Chrome

- Uncomment this line: `browser = webdriver.Chrome()`. (Uncommenting a line means removing the hashtag and empty space from its immediate left.) 
- Comment out this line: `browser = webdriver.Firefox()`. (Commenting out a line means adding a hashtag to its immediate left.)
- 

## License

This project is released under the MIT license. 