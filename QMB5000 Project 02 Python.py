
import nltk


RAW = '''
plot : two teen couples go to a church party , drink and then drive . they get into an accident . one of the guys dies , but his girlfriend continues to see him in her life , and has nightmares . what's the deal ? watch the movie and " sorta " find out . . . critique : a mind-fuck movie for the teen generation that touches on a very cool idea , but presents it in a very bad package . which is what makes this review an even harder one to write , since i generally applaud films which attempt to break the mold , mess with your head and such ( lost highway & memento ) , but there are good and bad ways of making all types of films , and these folks just didn't snag this one correctly . they seem to have taken this pretty neat concept , but executed it terribly . so what are the problems with the movie ? well , its main problem is that it's simply too jumbled . it starts off " normal " but then downshifts into this " fantasy " world in which you , as an audience member , have no idea what's going on . there are dreams , there are characters coming back from the dead , there are others who look like the dead , there are strange apparitions , there are disappearances , there are a looooot of chase scenes , there are tons of weird things that happen , and most of it is simply not explained . now i personally don't mind trying to unravel a film every now and then , but when all it does is give me the same clue over and over again , i get kind of fed up after a while , which is this film's biggest problem . it's obviously got this big secret to hide , but it seems to want to hide it completely until its final five minutes . and do they make things entertaining , thrilling or even engaging , in the meantime ? not really . the sad part is that the arrow and i both dig on flicks like this , so we actually figured most of it out by the half-way point , so all of the strangeness after that did start to make a little bit of sense , but it still didn't the make the film all that more entertaining . i guess the bottom line with movies like this is that you should always make sure that the audience is " into it " even before they are given the secret password to enter your world of understanding . i mean , showing melissa sagemiller running away from visions for about 20 minutes throughout the movie is just plain lazy ! ! okay , we get it . . . there are people chasing her and we don't know who they are . do we really need to see it over and over again ? how about giving us different scenes offering further insight into all of the strangeness going down in the movie ? apparently , the studio took this film away from its director and chopped it up themselves , and it shows . there might've been a pretty decent teen mind-fuck movie in here somewhere , but i guess " the suits " decided that turning it into a music video with little edge , would make more sense . the actors are pretty good for the most part , although wes bentley just seemed to be playing the exact same character that he did in american beauty , only in a new neighborhood . but my biggest kudos go out to sagemiller , who holds her own throughout the entire film , and actually has you feeling her character's unraveling . overall , the film doesn't stick because it doesn't entertain , it's confusing , it rarely excites and it feels pretty redundant for most of its runtime , despite a pretty cool ending and explanation to all of the craziness that came before it . oh , and by the way , this is not a horror or teen slasher flick . . . it's just packaged to look that way because someone is apparently assuming that the genre is still hot with the kids . it also wrapped production two years ago and has been sitting on the shelves ever since . whatever . . . skip it ! where's joblo coming from ? a nightmare of elm street 3 ( 7/10 ) - blair witch 2 ( 7/10 ) - the crow ( 9/10 ) - the crow : salvation ( 4/10 ) - lost highway ( 10/10 ) - memento ( 10/10 ) - the others ( 9/10 ) - stir of echoes ( 8/10 ) 
kolya is one of the richest films i've seen in some time . zdenek sverak plays a confirmed old bachelor ( who's likely to remain so ) , who finds his life as a czech cellist increasingly impacted by the five-year old boy that he's taking care of . though it ends rather abruptly-- and i'm whining , 'cause i wanted to spend more time with these characters-- the acting , writing , and production values are as high as , if not higher than , comparable american dramas . this father-and-son delight-- sverak also wrote the script , while his son , jan , directed-- won a golden globe for best foreign language film and , a couple days after i saw it , walked away an oscar . in czech and russian , with english subtitles . 
this three hour movie opens up with a view of singer/guitar player/musician/composer frank zappa rehearsing with his fellow band members . all the rest displays a compilation of footage , mostly from the concert at the palladium in new york city , halloween 1979 . other footage shows backstage foolishness , and amazing clay animation by bruce bickford . the performance of " titties and beer " played in this movie is very entertaining , with drummer terry bozzio supplying the voice of the devil . frank's guitar solos outdo any van halen or hendrix i've ever heard . bruce bickford's outlandish clay animation is that beyond belief with zooms , morphings , etc . and actually , it doesn't even look like clay , it looks like meat . 
`strange days' chronicles the last two days of 1999 in los angeles . as the locals gear up for the new millenium , lenny nero ( ralph fiennes ) goes about his business of peddling erotic memory clips . he pines for his ex-girlfriend , faith ( juliette lewis ) , not noticing that another friend , mace ( angela bassett ) really cares for him . this film features good performances , impressive film-making technique and breath-taking crowd scenes . director kathryn bigelow knows her stuff and does not hesitate to use it . but as a whole , this is an unsatisfying movie . the problem is that the writers , james cameron and jay cocks , were too ambitious , aiming for a film with social relevance , thrills , and drama . not that ambitious film-making should be discouraged ; just that when it fails to achieve its goals , it fails badly and obviously . the film just ends up preachy , unexciting and uninvolving . 
i had been expecting more of this movie than the less than thrilling twister . twister was good but had no real plot and no one to simpithize with . but twister had amazing effects and i was hoping so would volcano volcano starts with tommy lee jones at emo . he worrys about a small earthquake enough to leave his daughter at home with a baby sitter . there is one small quake then another quake . then a geologist points out to tommy that its takes a geologic event to heat millions of gallons of water in 12 hours . a few hours later large amount of ash start to fall . then . . . . it starts . the volcanic eruption . . . . i liked this movie . . . but it was not as great as i hoped . i was still good none the less . it had excellent special effects . the best view . . . the helecopters flying over the streets of volcanos . also . . . there were interesting side stories that made the plot more interesting . so . . . it was good ! ! 
'''

# Make all words lowercase and tokenize, show frequency in initial data
print("\n\nInitial Data")
RAW = RAW.lower()
the_Tokens   = nltk.tokenize.word_tokenize( RAW )
the_FreqDist = nltk.FreqDist( the_Tokens )
the_Counts   = the_FreqDist.most_common( 20 )
for c in the_Counts :
    print( c )

# Remove punctuation from the intial data and show frequency
print("\n\nRemove punctuation")
the_Tokens_02 = []
for t in the_Tokens :
    if t.isalpha() :
        the_Tokens_02.append( t )
the_FreqDist = nltk.FreqDist( the_Tokens_02 )
the_Counts   = the_FreqDist.most_common( 20 )
for c in the_Counts :
    print( c )

# Remove stop words and show show frequency
print("\n\nRemove stop words")
the_StopWords = nltk.corpus.stopwords.words("english")
the_Tokens_03 = []
for t in the_Tokens_02 :
    if t not in the_StopWords :
        the_Tokens_03.append( t )
the_FreqDist = nltk.FreqDist( the_Tokens_03 )
the_Counts   = the_FreqDist.most_common( 20 )
for c in the_Counts :
    print( c )

# Remove all words shorter than four characters
print("\n\nRemove words shorter less than 4 characters")
the_Tokens_04 = []
for t in the_Tokens_03 :
    if len(t) >= 4 : 
        the_Tokens_04.append( t )
the_FreqDist = nltk.FreqDist( the_Tokens_04 )
the_Counts   = the_FreqDist.most_common( 20 )
for c in the_Counts :
    print( c )




    


