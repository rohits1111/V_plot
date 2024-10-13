**Instructions**
1. We have mapped.bed.gz file which has the length between the gapping points and between a certain range; here it was approx 1000.
2. So here we have to plot a Scatter plot where we see a V plot.
3. for that, we read the mapped.bed.gz file and then using linear transformation rule to rescale the range between -500 to 500.
4. now sort the file and using uniq -c get the frequency of each position and length combination.
5. now write a python file which reads the data from file_name.tsv using pandas and plot the data using matplotlib.
**Execute**
1. now create a sh file using vim and write all the commands used to get the file which will be read by python file.
2. also the command for applying the python file to the file_name.tsv file.
3. finally save the file and execute the file using chmod +x file_name.tsv
4. now run the sh file using sh file_name.sh
5. finally and scatter plot will be observed where a V shape can be observed
