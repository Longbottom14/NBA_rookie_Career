# NBA_rookie_Career
**Rookie Career Prediction**

**Background**

This is my second NBA related project. The first project was NBA games prediction for 2021/22 season. [NBA 21/22 Prediction](https://github.com/Longbottom14/NBA_Analysis)

There is a common saying: _"first impression lasts longer"._ The first season of a NBA player is very crucial to their career on a long run.Some go on to become superstars, role players and some end up a bust.

And talking about contracts.. Rookie scale contracts are guaranteed for the first two years, with team options on the third and fourth years. What about the fifth year?

**Importance**

There is limited research investigating rookie career of basketball players. By improving the understanding of how long a rookie is going to last in the NBA. Rookies, franchises and agents can have some insights on what keep players in the NBA.

**Design, Setting, and Participants**

This retrospective cohort study used data from kaggle for training.( [training\_data](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats.))

Extracted publicly available data about NBA rookies between the 2016 to 2022 season from [fbref](https://hashtagbasketball.com/nba-rookie-rankings). Test data were scraped during this time frame using the beautifulsoup library. [scraping notebook](https://github.com/Longbottom14/NBA_rookie_Career/blob/master/notebooks/rookie_2020_to_2022_team_scraper.ipynb)

**Introduction**

The National Basketball Association (NBA) is the highest professional basketball league for men in North America.

NBA rookies are athletes who are competing in their first year in the professional league. Since 2006, players are required to be a minimum age of 19 years to be eligible for the NBA draft; as a result, more collegiate players have opted into the NBA draft after only 1 collegiate season, decreasing the mean draft age.

With younger players being drafted, rookie players may present with less physical maturation and have difficulty managing higher training loads and increased games per season. This difficulty in load management may reflect decreased fitness and development.

**Model.**

- **Experiment 1**

Pycaret library was used to obtain base models (logistic regression , Xgboost classifier , random forest classifier ,adaboost classifier ,lightgbm, Catboost and Gradientboost classifier)

Notebook : [pycaret notebook](https://github.com/Longbottom14/NBA_rookie_Career/blob/master/notebooks/Survival_NBA_Rookies_2.1_Pycaret.ipynb)

- **Experiment 2**

Features displayed high collinearity, _Multicollinearity reduces the precision of the estimated coefficients, which weakens the statistical power of your regression models._

I attempted techniques like Principal component analysis to reduce the multicollinearity. This didn't improve the model.

Feature creation didn't improve the model either, I tried multiple combinations, but the model accuracy didn't improve.

Notebook: [feature engineering](https://github.com/Longbottom14/NBA_rookie_Career/blob/master/notebooks/Survival_NBA_Rookies_2_Experiment1.ipynb)

- **Hyperparameter Tuning**

Hyper parameter tuning improved the model accuracy a little bit.

Notebook: [tuning](https://github.com/Longbottom14/NBA_rookie_Career/blob/master/notebooks/Survival_NBA_Rookies_4_Tuning.ipynb)

- **Model Blending & Stacking**

Blending the models improved the model accuracy and the performance was consistent across test data from different years

Notebook: [model blending](https://github.com/Longbottom14/NBA_rookie_Career/blob/master/notebooks/Survival_NBA_Rookies_5_Model_Blending.ipynb)

**Conclusion**

The first season projects the career of most NBA players. The level of competition is more intense in the NBA compared to the NCAA or college programs, as the rookies are going up against seasoned professional. It is very important if we are able to predict if a rookie career is going to be greater than 4 years in the NBA using only the first season stats.

**Deployment**

- Flask app: [Rookie-career.herokuapp.com](http://rookie-career.herokuapp.com/)

- Streamlit: [https://longbottom14-rookie-streamlit-main-3wctuf.streamlitapp.com/](https://longbottom14-rookie-streamlit-main-3wctuf.streamlitapp.com/)

**Acknowledgement**

I appreciate every one of you that made this project a success:

- Alexey Grigorev, Twitter: @AI\_grigor
- Hussain Ridwan, Twitter : @not\_rho
- Akinwa Lekan, Twitter : @AkinwaLekan , github : https://github.com/lekzy455
- Akorode Adewole, Twitter : @\_manofletters , github : [https://github.com/Akorex](https://github.com/Akorex) , kaggle : Akorode Adewole
