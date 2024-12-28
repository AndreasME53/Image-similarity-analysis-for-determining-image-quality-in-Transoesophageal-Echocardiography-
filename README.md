## Desription 

This is a notebook that I worked on in which I do Image similarity analysis for determining image quality in Transoesophageal Echocardiography.

I have 4 key questions that I want to answer:

#### Question 1: 
  Considering the two different image quality scores (general impression, criteria percentage): 
    i) To calculate this the Pearson correlation coefficient for the two scores for each view. Identify for which view the two scores are in higher agreement.
    ii) For each view, perform linear regression analysis for the two image quality scores (use general impression as dependent and criteria percentage as independent). Compute the 
        RMSE and R2 scores and comment on the performance of  regression. Plot the regression output only for the three best performing cases.
    iii) Plot the true vs estimated values for three best performing views and comment on the model performance for two different general impression score ranges (0-2, 2-4). 

#### Question 2:
  We are interested in evaluating the content similarity of the test images against the gold standard ones. To perform this, we will use three key statistical metrics developed to compare 
  the content between two images. 
    i) To calculate this and list the SSI, MI and CS values for each test image against the gold standard
       ones (use the scikit-imag, scikit-learn, scipy libraries). Identify the top three test images (which 
       participant) for each view that have the most similar content to the gold standard ones 
       according to their SSI, MI and CS values.
    ii) For each view develop a hypothesis and perform a statistical test to evaluate the differences 
        between the expert and novice groups in terms of SSI, MI and CS. List and discuss  
        results in terms of significance. Which similarity metric out of the three better captures the 
        differences between expert and novice surgeons?

#### Question 3 
    Considering the extracted SSI, MI, and CS values:  
      i) To calculate this the correlation coefficient for SSI and MI, SSI and CS, and MI and CS for each 
         view. Identify for which view, in each pair, the two parameters are in higher agreement. 
      ii) Perform polynomial regression using a 7th degree order polynomial for the SSI, MI, and CS 
          against both the criteria percentage and general impression for each view (SSI/MI/CS – 
          independent, manual scores – dependent). In case this leads to overfitting use a regularization 
          method (LASSO, RIDGE or Elastic Net regression) and identify the optimal degree of the 
          polynomial to avoid overfitting. Justify  selection for the regularization method. To calculate this  
          and list the RMSE and R2 scores of  regularized regression. Identify the three views for 
          which the regularized regression performs better. Plot the regression output only for the three 
          best performing cases. Consider correlation coefficients smaller than 0.01 as not contributing 
          to  regression.
      iii) Perform linear regression using Gaussian basis for the SSI against the criteria percentage 
          for each view (SSI – independent, criteria percentage – dependent). Decide the order of the 
          gaussian basis, so that the regression model will not underfit/overfit (can also use a 
          regularizer). To calculate this and list the RMSE and R2 scores of  regularized regression. Identify 
          the three views for which the regularized regression performs better. Plot the regression output 
          only for the three best performing cases.
          
#### Question 4 
  A good quality US image means that the heart structures are 
  correctly placed in the centre. To evaluate this, To calculate this the misalignment of the test images 
  against the gold standard ones.
    i) To calculate this and list the rotation (in degrees) and translation values (in pixel units) of the rigid 
       transformation (use the opencv library) between the test and gold standard images
    ii) For each view develop a hypothesis and perform a test to evaluate the differences between 
        the expert and novice groups in terms of the values of rotation and translation. List and discuss 
         results in terms of significance.
    iii) Perform linear regression for the rotation and translation against both the criteria 
         percentage and general impression (rotation/translation – independent, manual scores – 
         dependent) for each view. To calculate this  and list the RMSE and R2 scores of  regression. 
         Identify the three views for which the linear regression performs better in every combination 
         of independent/dependent variables. Plot the regression output only for the three best 
         performing cases. 









