import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Text to be converted to audio
text = """
Halloween began with the Celtic festival of Samhain, celebrated around 2,000 years ago. Samhain, meaning “summer’s end” in Old Irish, 
was the most important of the four major festivals in the Celtic calendar. Marking the end of the harvest and the beginning of winter, 
it fell on October 31 and symbolized the transition into the darker half of the year.

The Celts believed that on this night, the boundaries between the world of the living and the spirit world weakened, 
allowing souls, spirits, and supernatural beings to roam freely on Earth. This spiritual “crossing” of worlds could be helpful 
or harmful, so people left food offerings outside their homes to appease wandering spirits. They also wore costumes and animal 
masks to disguise themselves from any malevolent spirits and avoid supernatural tricks.

Large communal bonfires were central to Samhain. Villagers would extinguish their home fires and relight them from the communal 
blaze as a symbol of unity and protection. Celts gathered around the bonfire, making sacrifices of crops or animals to appease 
their gods, and these fires were thought to protect them through the harsh winter.

When the Romans conquered much of Celtic territory by 43 AD, they brought their own traditions, blending them with local customs. 
They introduced their own festivals, including Feralia, a day in late October when Romans honored the dead, and Pomona, a festival 
dedicated to the goddess of fruit and trees. Pomona’s symbol was the apple, likely the origin of today’s Halloween tradition of 
bobbing for apples.

By the 8th century, Christianity had spread into Celtic lands, and the church was attempting to replace pagan festivals with 
Christian observances. Pope Gregory III moved All Saints’ Day to November 1 in an effort to assimilate the Samhain customs, 
framing it as a time to honor saints and martyrs. The evening before was known as All Hallows’ Eve, which eventually became Halloween.

Later, November 2 became All Souls’ Day, a day to honor the dead. This three-day observance—All Hallows’ Eve, All Saints’ Day, 
and All Souls’ Day—was known as Hallowtide. During this period, many people in Europe would dress up as saints, angels, or devils, 
a tradition that echoed Samhain’s spirit of warding off harmful entities.

During the Middle Ages, a practice called “souling” began in England. Poor children and adults would go door-to-door, offering 
prayers for deceased loved ones in exchange for soul cakes (small pastries). This custom is thought to be an early influence 
on modern trick-or-treating, as people went door-to-door asking for treats.

Another tradition called “mumming,” or performing short skits, also became common in Ireland and Britain. People dressed in 
costumes and went house-to-house singing, dancing, or reciting poetry in exchange for food and drink, which later evolved into 
some aspects of trick-or-treating as we know it.

In Ireland and Scotland, people began carving faces into turnips, beets, or potatoes to ward off a spirit named Stingy Jack, 
a popular folk figure. According to legend, Jack was a trickster who deceived the devil and was doomed to wander the earth with 
only a burning coal inside a carved-out turnip to light his way. The tradition evolved when immigrants brought it to North America, 
where they found pumpkins—a native fruit—perfect for carving. Thus, the Jack-o’-Lantern was born.

Halloween arrived in North America with Irish and Scottish immigrants in the 19th century. Early American Halloween celebrations 
were more about community gatherings, storytelling, and fortune-telling. In the 1920s and 1930s, Halloween parties for both children 
and adults became common, focusing on games, seasonal foods, and costumes.

The practice of trick-or-treating evolved during this time. Some say it was a way to keep children from engaging in Halloween 
pranks, a tradition that became rowdy in many communities. By the 1950s, Halloween was firmly rooted as a child-centered celebration, 
with costumes, candy, and neighborhood trick-or-treating defining the holiday.

Today, Halloween is celebrated in much of the Western world, evolving into a fun, imaginative holiday with spooky decorations, 
candy, haunted houses, and costume parties. In the U.S. alone, people spend billions each year on Halloween festivities, making it 
one of the most popular holidays. The holiday has come full circle from its origins, blending ancient customs, religious observances, 
and modern commercialism into a single, cohesive celebration.

From a spiritual festival of life, death, and harvest to a community-wide, child-centered celebration, Halloween is rich with history 
and symbolism that connects the present to a distant, mystical past.
"""

# Set properties for the audio
engine.setProperty('rate', 150)  # Set speech rate
engine.setProperty('volume', 1)  # Set volume level between 0 and 1

pyttsx3.speak(text)