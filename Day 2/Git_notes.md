### Git 

#### What is Git?
Git is an open source distributed version control system (VCS) designed to handle everything from small to very large projects with speed and efficiency. Through this we are able to track changes and manage files. Git does not store data in a file based system, it stores information in the form of snapshots.
<br>
<br>
With Git everytime you commit, save the state of your project,it takes a picture of what all your files look like at that moment and stores a reference to that snapshot. In Addition, for efficiency, if you haven't made any changes to the files, Git does not store that file again. 

<img height="300" src="C:\Users\Prismika\PycharmProjects\pythonbasic\Day 2\data_as_snapshots_GIT.png" width="800"/> 
<br> Figure 1.Storing data as snapshots of the project over time

#### The Three States 
Git has three main states that your file can reside in: 
- **Modified**
<br> 
This means that when you make changes to a file in your Git repository, it becomes "modified" because it contains new changes compared to the version that was last committed. These changes have not yet been saved to the staging area.
<br>




- **Staged**
<br>
Staging is the step before committing your changes. This is where you prepare your files to be included in the next commit. When you have made changes to a file, and you want to include those changes in the next commit, you 'stage'the file. 


- **Committed** 
<br> 
After you have staged your changes, you commit them. This means you are taking a snapshot/ saving of the current state of your project, including all staged changes. These changes are now saved in the Git repository and can be accessed anytime. 


