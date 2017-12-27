Python 2.5.1 (r251:54869, Apr 18 2007, 22:08:04) 
[GCC 4.0.1 (Apple Computer, Inc. build 5367)] on darwin
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2.1      
>>> ================================ RESTART ================================
>>> 
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  q p b u d h o
Enter word, or a . to indicate that you are finished: bud
bud earned 6 points. Total: 6 points
Current Hand:  q p h o
Enter word, or a . to indicate that you are finished: a
Invalid word, please try again.
Current Hand:  q p h o
Enter word, or a . to indicate that you are finished: .
Total score: 6 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: 
>>> ================================ RESTART ================================
>>> 
bud earned 6 points. Total: 6 points
What is your name?: g
It took 9.598 to enter your name
>>> ================================ RESTART ================================
>>> 
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  u t t g f k o
Enter word, or a . to indicate that you are finished: got
got earned 0.941294965514 points. Total: 0.941294965514 points It took 4.24946498871 to enter the word
Current Hand:  u t f k
Enter word, or a . to indicate that you are finished: n
Invalid word, please try again.
Current Hand:  u t f k
Enter word, or a . to indicate that you are finished: .
Total score: 0.941294965514 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  a p y v i h k
Enter word, or a . to indicate that you are finished: hip
hip earned 0.732060542377 points. Total: 0.732060542377 points It took 10.928057909 to enter the word
Current Hand:  a y v k
Enter word, or a . to indicate that you are finished: kay
kay earned 0.701207053658 points. Total: 1.43326759604 points It took 14.261122942 to enter the word
Current Hand:  v
Enter word, or a . to indicate that you are finished: a
Invalid word, please try again.
Current Hand:  v
Enter word, or a . to indicate that you are finished: v
Invalid word, please try again.
Current Hand:  v
Enter word, or a . to indicate that you are finished: .
Total score: 1.43326759604 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  c r e e d y l
Enter word, or a . to indicate that you are finished: red
red earned 0.706417482515 points. Total: 0.706417482515 points It took 5.66237401962 to enter the word
Current Hand:  c e y l
Enter word, or a . to indicate that you are finished: ley
ley earned 0.991697206709 points. Total: 1.69811468922 points It took 6.05023384094 to enter the word
Current Hand:  c
Enter word, or a . to indicate that you are finished: 
>>> ================================ RESTART ================================
>>> 

Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  x e t g v y u
Enter word, or a . to indicate that you are finished: get
get earned 1.34353123704 points. Total: 1.34353123704 points It took 2.977 seconds to enter the word
Current Hand:  x v y u
Enter word, or a . to indicate that you are finished: vux
Invalid word, please try again.
Current Hand:  x v y u
Enter word, or a . to indicate that you are finished: yuv
Invalid word, please try again.
Current Hand:  x v y u
Enter word, or a . to indicate that you are finished: ux
Invalid word, please try again.
Current Hand:  x v y u
Enter word, or a . to indicate that you are finished: .
Total score: 1.34353123704 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  b e g h m o n
Enter word, or a . to indicate that you are finished: 
>>> ================================ RESTART ================================
>>> 

Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
n
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  a a g g g w t
Enter word, or a . to indicate that you are finished: tag

Traceback (most recent call last):
  File "/Users/johnrom/Desktop/6.00 Intro to Programming/ps5SOL.py", line 281, in <module>
    play_game(word_list)
  File "/Users/johnrom/Desktop/6.00 Intro to Programming/ps5SOL.py", line 266, in play_game
    play_hand(hand.copy(), word_list)
  File "/Users/johnrom/Desktop/6.00 Intro to Programming/ps5SOL.py", line 231, in play_hand
    print "It took %0.3f seconds to enter the word" % total_time
UnboundLocalError: local variable 'total_time' referenced before assignment
>>> ================================ RESTART ================================
>>> 
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand:  x u m o v v v
Enter word, or a . to indicate that you are finished: 
Invalid word, please try again.
Current Hand:  x u m o v v v
Enter word, or a . to indicate that you are finished: vom
Invalid word, please try again.
Current Hand:  x u m o v v v
Enter word, or a . to indicate that you are finished: vox
It took 2.664 seconds to enter the word
vox earned 4.88036551129 points. Total: 4.88036551129 points
Current Hand:  u m v v
Enter word, or a . to indicate that you are finished: 
