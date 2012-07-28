library("RMySQL")



m<-dbDriver("MySQL")

conn <-dbConnect(m, dbname = 'newsright') 

results <-dbSendQuery(conn, "select half_life from half_life_count where half_life < 50")

data = fetch(results, n = -1)

dim(data)

hist(as.numeric(data[,1]), plot=FALSE)
H <- hist(as.numeric(data[,1]), plot=FALSE)


CATEGORIES
results <-dbSendQuery(conn, "select count(*) as count, B.category from half_life_count A left join categories B ON A.storykey = B.storykey GROUP BY B.category")

categoryCounts = fetch(results, n = -1) 


#############################################
pdf(file='/home/ubuntu/newsright/plots/half_life_cat_run1.pdf')

 i = 1
  
  results =  dbSendQuery(conn, "select half_life from half_life_count")
  data = fetch(results, n = - 1)
  Full = hist(as.numeric(data[,1]),plot = FALSE)
  breaks = Full$breaks

  mids = Full$mids

  c = 10000
   
    plot(mids, Full$counts/c, col = i, type='l', main='Half-Life by Category', ylab="Percentage per Category", xlab= "Half-Life in Hours")
     
      par(new=TRUE)
       
       for(cat in categoryCounts$category){
            
                
                    
                        i = i + 1
                            
                                results <- dbSendQuery(conn, paste("select half_life from half_life_count A left join categories B  ON A.storykey = B.storykey WHERE B.category = '",cat,"'" , sep='') )

                                    data = fetch(results, n = -1)
                                        
                                            c = categoryCounts$count[which(categoryCounts$category == cat)]

                                                H <- hist(as.numeric(data[,1]), plot = FALSE, breaks = breaks)
                                                    
                                                        plot(mids, H$counts/c, col = i, type='l', axes= FALSE, ylab='', xlab='')
                                                            
                                                                par(new=TRUE)
                                                                    
       }


       legend('topright', c("All", categoryCounts$category), col = c(1:16), lty=1:1)

       dev.off()
###################################################

       COUNTS

       results <-dbSendQuery(conn, "select count from half_life_count where count < 200")

       data = fetch(results, n = -1)

       hist(data[,1], plot = FALSE)


