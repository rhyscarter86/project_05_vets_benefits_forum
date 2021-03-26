# project_05

# Understanding Activity on VetsBenefits.net

This effort looks at roughly 8,000 posts, ranging in size from 1-2 sentences, up to 1 or more paragraphs, on VetsBenefits.net.  VetsBenefits.net is a web forum where Veterans can ask questions about Veterans Benefits Administration (VBA) benefit programs, and get support for issues they may be experiencing navigating different benefits. The site is broken out into multiple sub-pages, each with 1 or more threads (a thread being a user-initiated topic for discussion), and each of those with one or more subsequent replies.

## Description and Data Used

Data was collected for the 500 most recently active threads. Active threads consisted mostly of January through March, although some threads maintained activity going back one or more years. To ensure more consistent and manageable data analysis and comparisons for weeks, data going back to September 2019 was selected to provide roughly 6 months of pre-Covid data, as well as capture activity during the pandemic.

## Overall Outcome

*Anchoring on several different areas including Covid, Disability & Appeals, Mental Health, the Aid & Attendance program, and Sleep related issues, CorEx topic modeling identified 5 additional topics for further investigation.*

![corex_topics](images/screenshot1.png)

## Features & Techniques Used

* Data was vectorized via Countvectorizer, then Non-negative Matrix Factorization (NMF) with triplet-grams was used to create features for all ~50k tweets

## Tools & Techniques Used

#### *For Data Collection and EDA:*
* Twint Package
* Python Jupyter Notebook
* Pandas and Numpy
* Tableau

#### *For Matrix Factorization and Topic Modeling*
* Scikit-Learn NMF
* TF-IDF
* Countvectorizer

## Workbooks
* File0 - Data Acquisition: Data collection via Twint and initial file pickling for downstream use.
* File1 - Data Cleaning: Pre-processing of tweets, including removing special characters, combining named entities, and removing duplicates.
* File2 - EDA and Prelim Visualizations: Initial EDA, particularly around dates and corresponding visualizations of time series for VA tweets.
* File3 - Vectorization and Topic Modeling: Vectorization and Topic Modeling, with appendix containing other versions of both that were tested prior to settling on final.
* File4 - Reference Scratch Notebook: Draft workbook for reference.

## Analysis Limitations

* **Limited timeframe to ensure speed and limit complexity given time constraints** 6 months of data vs. a whole year was a deliberate decision to try and reduce complexity and ensure completion of efforts. However, doing so did limit the conclusions able to be drawn. An expansion of this analysis is planned to ensure year over year comparisons are possible.

## Possible Impacts & Future Efforts

There are clear implications for gaining a better understanding of the Veteran community's needs and current concerns. While VA may have its messaging, this may or may not align with what Veterans themselves are most concerned with. This effort seeks to bridge that gap. Additionally, gaining an understanding of who the Veterans are currently using Twitter, as well as who may be influential, presents additional opportunities for more targeted Veteran outreach and effective communications.  

#### *Future Efforts:*
Expand the use of not just Twitter data, but other hubs of Veteran communications, including message boards, Reddit threads, and others.
