library("RMySQL")
library('ggplot2')

m<-dbDriver("MySQL")

conn <-dbConnect(m, dbname = 'newsright') 

results <-dbSendQuery(conn, "select half_life from half_life_count where half_life < 50")

data = fetch(results, n = -1)

dim(data)

hist(as.numeric(data[,1]), plot=FALSE)
H <- hist(as.numeric(data[,1]), plot=FALSE)

## 
## CATEGORIES
results <-dbSendQuery(conn, "select count(*) as count, B.category from half_life_count A left join categories B ON A.storykey = B.storykey GROUP BY B.category")

categoryCounts = fetch(results, n = -1) 


#############################################
getdataHL <- function(minhalflife = 0, maxhalflife = 0) {
    query = "select half_life from half_life_count "
    if (maxhalflife > 0) {
        query = paste(query, 'where half_life <', maxhalflife)
    } 
    if (minhalflife > 0) {
        query = paste(query, 'AND half_life >=', minhalflife)
    } 
    print (query)
    results =  dbSendQuery(conn, query)
    data = fetch(results, n = - 1)
    Full = hist(as.numeric(data[,1]),plot = FALSE)
    breaks = Full$breaks    
    mids = Full$mids

    c = 20000

    plotdata = data.frame(name = c(), pcount = c(), mids = c() )

    pd = data.frame(name = 'Full', pcount = Full$counts / c, mids = mids)

    plotdata = rbind(plotdata, pd)

                                                                                                       
    for(cat in categoryCounts$category){
        query = paste("select half_life from half_life_count A left join categories B  ON A.storykey = B.storykey WHERE B.category = '",cat,"'" , sep='') 
                                                                                                                                 
        if (maxhalflife > 0) {
           query = paste(query, 'AND half_life <', maxhalflife)
        }
        if (minhalflife > 0) {
            query = paste(query, 'AND half_life >=', minhalflife)
        } 
                  
        results <- dbSendQuery(conn, query )

        data = fetch(results, n = -1)
                                                  
        c = categoryCounts$count[which(categoryCounts$category == cat)]
          
        H <- hist(as.numeric(data[,1]), plot = FALSE, breaks = breaks)
                       
        pd = data.frame(name = cat, pcount = H$counts / c, mids = mids)
        plotdata = rbind(plotdata, pd)
    }
    return (plotdata)
}

getHLByWebsite <- function(minhalflife = 0, maxhalflife = 0) {
    query = "select half_life from half_life_count"
    if (maxhalflife > 0) {
        query = paste(query, 'where half_life <', maxhalflife)
    } 
    if (minhalflife > 0) {
        query = paste(query, 'AND half_life >=', minhalflife)
    } 
    print (query)
    results =  dbSendQuery(conn, query)
    data = fetch(results, n = - 1)
    Full = hist(as.numeric(data[,1]),plot = FALSE)
    breaks = Full$breaks    
    mids = Full$mids

    c = 20000

    plotdata = data.frame(name = c(), pcount = c(), mids = c() )

    pd = data.frame(name = 'Full', pcount = Full$counts / c, mids = mids)

    plotdata = rbind(plotdata, pd)

    websites = c('newstimes.com', 
    'ctpost.com',
    'hosted.ap.org',
    'www.huffingtonpost.com',
    'hosted2.ap.org',
    'apnews.com',
    'www.sfgate.com',
    'mysanantonio.com',
    'timesunion.com',
    'chron.com')
                                                                                                       
    for(website in websites){
        query = paste("select half_life from half_life_count A left join story_info B ON A.storykey = B.storykey WHERE B.website= '",website ,"'" , sep='') 
                                                                                                                                 
        if (maxhalflife > 0) {
           query = paste(query, 'AND half_life <', maxhalflife)
        }
        if (minhalflife > 0) {
            query = paste(query, 'AND half_life >=', minhalflife)
        } 
                  
        results <- dbSendQuery(conn, query )

        data = fetch(results, n = -1)
                                                  
        c = nrow(data) 
          
        H <- hist(as.numeric(data[,1]), plot = FALSE, breaks = breaks)
                       
        pd = data.frame(name = website, pcount = H$counts / c, mids = mids)
        plotdata = rbind(plotdata, pd)
    }
    return (plotdata)
}

getdataCounts <- function(mincount = 0, maxcount = 0) {
    query = "select count from half_life_count "
    if (maxcount > 0) {
        query = paste(query, 'where count <', maxcount)
    } 
    if (mincount > 0) {
        query = paste(query, 'AND count >=', mincount)
    } 
    print (query)
    results =  dbSendQuery(conn, query)
    data = fetch(results, n = - 1)
    Full = hist(as.numeric(data[,1]),plot = FALSE)
    breaks = Full$breaks    
    mids = Full$mids

    plotdata = data.frame(name = c(), pcount = c(), mids = c() )

    pd = data.frame(name = 'Full', pcount = Full$counts, mids = mids)

    plotdata = rbind(plotdata, pd)


    for(cat in categoryCounts$category){
        query = paste("select count from half_life_count A left join categories B  ON A.storykey = B.storykey WHERE B.category = '",cat,"'" , sep='') 

        if (maxcount > 0) {
            query = paste(query, 'AND count <', maxcount)
        }
        if (mincount > 0) {
            query = paste(query, 'AND count >=', mincount)
        } 

        results <- dbSendQuery(conn, query )

        data = fetch(results, n = -1)

        c = categoryCounts$count[which(categoryCounts$category == cat)]

        H <- hist(as.numeric(data[,1]), plot = FALSE, breaks = breaks)

        pd = data.frame(name = cat, pcount = H$counts, mids = mids)
        plotdata = rbind(plotdata, pd)

    }
    return (plotdata)
}

plotbycategory <-function(min, max, filename, type, title) {

    if(type == 'HL'){plotdata <- getdataHL(min, max)}
    if(type == 'Counts'){plotdata <- getdataCounts(min, max)}

    print(plotdata)
    pdf(file = filename)

    split <- which(plotdata$name == 'Health')[1] - 1

    p1 <- ggplot(plotdata[1:split,], aes(x = mids, y = pcount, group = name, color = name))
    p1 <- p1 + scale_colour_brewer(palette="Paired")
    p1 <- p1 + labs(colour = "Categories")
    p1 <- p1 + opts(title = title)

    if(type == 'HL'){
        p1 <- p1 + scale_x_continuous('Half-life in Hours') + scale_y_continuous('Percentage of Counts')
    }
    if(type == 'Counts'){
        p1 <- p1 + scale_x_continuous('Impression Counts') + scale_y_continuous('Percentage of Counts')
    }

    p1 <- p1 + geom_line() 

    print(p1)

    p2 <- ggplot(plotdata[split + 1:nrow(plotdata),], aes(x = mids, y = pcount, group = name, color = name))
    p2 <- p2 + scale_colour_brewer(palette="Paired")
    p2 <- p2 + labs(colour = "Categories")
    p2 <- p2 + opts(title = title)

    if(type == 'HL'){
        p2 <- p2 + scale_x_continuous('Half-life in Hours') + scale_y_continuous('Percentage of Counts')
    }
    if(type == 'Counts'){
        p2 <- p2 + scale_x_continuous('Impression Counts') + scale_y_continuous('Percentage of Counts')
    }

    p2 <- p2 + geom_line() 

    print(p2)

    dev.off()

}


data <- getHLByWebsite(24, 250)
print (data)
#plotbycategory(0, '/home/ubuntu/newsright/plots/half_life_cat_all2.pdf', 'Half-Life by Category')

#plotbycategory(48, 3000, '/home/ubuntu/newsright/plots/half_life_cat_all_3000.pdf', 'Half-Life by Category, max 3000 hours')

#plotbycategory(48, 1000, '/home/ubuntu/newsright/plots/half_life_cat_all_1000.pdf', 'Half-Life by Category, max 1000 hours')

#plotbycategory(0, 100, '/home/ubuntu/newsright/plots/half_life_cat_all_100.pdf', 'Half-Life by Category, max 100 hours')

#plotbycategory(24, 3000, '/home/ubuntu/newsright/plots/half_life_cat_all_3000_V2.pdf', 'HL', 'Half-Life by Category, 24 - 3000 hours')

#plotbycategory(10, 10000, '/home/ubuntu/newsright/plots/counts_cat_all_max10000.pdf', 'Counts', 'Impression Counts by Category, max 10000')
