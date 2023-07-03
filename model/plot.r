library(tidyverse)

df <- read_csv("predictions.csv")

df %>% ggplot(aes(x=real, y=prediction)) +
    geom_abline(slope=1, linetype="dashed", color="grey") +
    geom_point() +
    xlim(0,1) +
    xlab("ABM p_eat") +
    ylab("predicted p_eat") +
    theme(panel.grid.major = element_blank(), 
          panel.grid.minor = element_blank(),
          panel.background = element_blank(), 
          axis.title = element_text(size = 8), 
          axis.line = element_line(colour = "black"))
    

ggsave("predictions.pdf", width=2, height=2)

