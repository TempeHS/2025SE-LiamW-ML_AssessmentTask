# Data Records

Recording the changes to the data such as scaling and encoding so it can be correctly applied to new incoming data. This will include anything done to the data in data wrangling and feature engineering

## Scaled Data

| Data         | Min/Max   | Scale Min/Max |
| ------------ | --------- | ------------- |
| Global_Sales | 0.01/1.1  | 0/1.2         |
| NA_Sales     | 0.00/0.4  | 0/1.2         |
| EU_Sales     | 0.00/0.15 | 0/1.2         |
| JP_Sales     | 0.00/0.07 | 0/1.2         |
| Other_Sales  | 0.00/0.02 | 0/1.2         |

## Encoded Data

| Data  | Unencoded                                                                                                                                                                                                       | Genre_Action | Genre_Adventure | Genre_Fighting | Genre_Misc | Genre_Platform | Genre_Puzzle | Genre_Racing | Genre_Role-Playing | Genre_Shooter | Genre_Simulation | Genre_Sports | Genre_Strategy |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | -------------- | ---------- | -------------- | ------------ | ------------ | ------------------ | ------------- | ---------------- | ------------ | -------------- |
| Genre | <ul><li>Action</li><li>Adventure</li><li>Fighting</li><li>Misc</li><li>Platform</li><li>Puzzle</li><li>Racing</li><li>Role-Playing</li><li>Shooter</li><li>Simulation</li><li>Sports</li><li>Strategy</li></ul> | True/False   | True/False      | True/False     | True/False | True/False     | True/False   | True/False   | True/False         | True/False    | True/False       | True/False   | True/False     |

## Engineered Features

| Data       | Engineering                                                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Popularity | data_frame['popularity'] = 100 \* (((data_frame['NA_Sales']/0.5)/186.28 + (data_frame['EU_Sales']/0.2) / 467.334 + (data_frame['JP_Sales']/0.1) / 36.276 + (data_frame['Other_Sales']/0.05) /1430.435) / 4 ) |
|            |                                                                                                                                                                                                              |
|            |                                                                                                                                                                                                              |
