Welcome to our project! We are called Phase 4 Ground. We were founded to
produce an ensemble of open source digital solutions for “Five and
Dime”, the 5GHz uplink and 10GHz downlink strategy for upcoming digital
payloads from AMSAT.

Phase 4 Ground is working to produce both a manufactured solution and a
set of documents that fully enable motivated operators to build their
own gear or assemble a station from commonly available parts and SDR
products. These radios will be modern, capable, flexible, and fun! No
crappy codecs, no confusing user interfaces.

Why microwave? Relatively small antennas and big bandwidths, and if we
don’t get more people on the microwave bands, we risk losing them. Why
digital? Too many advantages to list!

But wait, there’s more! Phase 4 Ground radios aren’t just for satellites
and space. These radios will also work terrestrially. Instead of a
satellite, you would use a Groundsat on a mountaintop or tower. You
would get all of the really interesting and fun services that the
powerful payload provides, but on the ground instead of in space.
Point-to-point communications on 10GHz looks entirely possible and is
being actively discussed. This means you don’t have to be geographically
close to a mountaintop Groundsat to work someone terrestrially.

So what have we done so far?

We split this team off from the space payload teams to avoid ITAR. It is
open to all.

We demonstrated frequency division multiple access uplink to time
division multiplex downlink using GNU Radio and USRPs. We have just
scratched the surface of what GNU Radio can do for us.

We will support legacy analog radios through an optional radio
peripheral called an Amateur Radio Access Point. Similar to Wires-X,
analog radio traffic is digitized and then intelligently tagged to
become part of the distributed digital downlink stream. People with NBFM
HTs can play with us!

We have identified and adopted a framework. Phase 4 Ground uses
standards from https://www.dvb.org. We’re using DVB-S2X for space,
DVB-T2 for terrestrial, GSE for low-overhead encapsulation of digital
data, and we are going to implement adaptive coding and modulation. Your
radio will use the best code and modulation scheme it can, in order to
maximize throughput!

The DVB standards provide very well thought out solutions to the most
common problems of digital transmission. However, the decision to adopt
them does not mean we’re finished. On the contrary! Implementing the
standard in a ham-centric way requires figuring out what options are
unnecessary, what needs to be modified, and what additional mechanisms
need to be designed.

However, that’s just the tip of the iceberg. The RF chain has challenges
too. Remember the choice of frequencies? That 5GHz uplink has a second
harmonic that just happens to be within the range of the sorts of LNBs
that we’d really like to use on 10GHz. A dual band feed from Paul Wade
W1GHZ has been designed and simulated. We look forward to building and
testing it!

Another challenge that digital communication brings is the possibility
of access control. Digital systems provide a means for identifying,
authenticating, and authorizing access to a communications resource. We
have adopted a Logbook of the World approach to authentication, and
support several approaches to authorization. Next? Implement and test!

Phase 4 Ground team currently consists of nearly 100 volunteers that
have signed up to work on the project. “Work” ranges from building
equipment, calculating things that need calculating, finding the best
existing solution to adapt to our project, reviewing documents for dumb
mistakes, making communications happen, blank paper engineering,
cheerleading, designing beautiful graphical user interfaces,
evangelizing, fundraising, documenting, providing adult supervision,
programming, meeting people that might provide us services we need,
updating the documentation, more programming, coming up with algorithms,
and many other roles and responsibilities. We have a lot of fun and we
want to share the fun with you.

We’ve accomplished a lot but have a long way to go! We need you!

All our documents and software are and will be at our github account at
<https://github.com/phase4ground>

Our Slack is  
<http://phase4ground.slack.com>  
  
And, we have a mailing list.  
  
Want to join Phase 4 Ground engineering?

Contact Michelle at <mountain.michelle@gmail.com> and we’ll get you
started!
