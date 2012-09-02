setwd('/Users/mdeland/kfit/Blok')

data <- read.csv('sorted_starbucks_impressions.csv', sep = '|', header = FALSE)

title <- "Locations of Starbucks/Square Related Impressions"

names(data) <- c('story', 'geoid', 'time', 'browser', 'country', 'state', 'zip', 'lon', 'lat')
head(data)
library(ggplot2)
library(maps)

all_states <- map_data("state")
#plot all states with ggplot
p <- ggplot()
p <- p  + geom_polygon( data=all_states, aes(x=long, y=lat, group = group),colour="white", fill="grey")
#p <- p  + geom_point( data=data, aes(x=lon, y=lat, size = NumContacts, alpha = NumContacts, color = NumContacts)) + scale_size(name="NumContacts", range = c(1,22))
p <- p  + geom_jitter( data=data, position = position_jitter(width = .5, height = .5), aes(x=lon, y=lat))
#p <- p  + scale_colour_gradient(low = "blue", high = "green")
p <- p  + coord_cartesian(xlim=c(-130, -65), ylim=c(25, 50)) 
p <- p + opts(legend.position = "none") 
p <- p + opts(title = title)
p