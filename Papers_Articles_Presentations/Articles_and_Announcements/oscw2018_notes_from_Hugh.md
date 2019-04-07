                         ______________________

                          NOTES FROM OSCW 2018

                               Hugh Brown
                         ______________________


Table of Contents
_________________

1 Overall
2 [2018-09-24 Mon]
3 [2018-09-25 Tue]


1 Overall
=========

  - Many (not all) of the presentations about actual cubesat projects
    could be best described as "case studies" -- mention (often in
    passing) of having used open source tools for design, simulation,
    etc
    - Heavy representation from university projects; next biggest
      contingents were (I think) community projects (SatNOGS, etc) or
      space agencies (ESA, NASA)
    - Would be great to see more companies presenting or even just
      attending (which I've passed on to organizers), for a change of
      perspective; still learning the field, though, and perhaps there
      simply aren't that many that are interested
  - Two presentations of visualization tools for space missions (OpenMCT
    + SatNOGS) -- very good to see this, as the focus on UX/UI is often
    a weak point in Open Source and makes a huge difference for ease of
    adoption
  - As designs for antenna progress, it will be worth talking to SatNOGS
    folks about designs/instructions for easy-to-build Phase 4 antenna
    that can be put into SatNOGS ground stations
    - One interesting possibility might be to market Phase4 radio
      designs (or better yet, cubesat parts as Bruce has suggested) +
      SatNOGS ground station as a standard open source ground station
      for satellite telemetry:
      - visualization via SatNOGS DB
      - telemetry/instrument data via DVB
      - perhaps with built-in amateur radio functionality (whatever the
        next generation of current AMSAT FM repeaters might look like)
        in order to get amateur radio community interested as well
        (though this may need to be balanced against worries of amateur
        radio folks appearing as scribes/assistants)
      - Note: C&C not part of SatNOGS; they've got some stubs for the
        functionality, but I'm not sure if this is a priority for them
  - Still a lot of open questions about physical/mechanical/electrical
    standards (Hyper-cube, pc104); this may complicate ability to
    provide a board/plan that's anything like "this size fits most"
    - Note: I'm not entirely sure if this has been a priority for the
      project.  My knowledge of mechanical/electrical engineering is
      *incredibly* limited, and I have a lot of questions.
  - Some knowledge about Phase 4 Ground project, but not a huge amount
    - This may have been due to the attendees (skewed heavily toward
      academic institutions, researchers) and/or my choice of who i
      talked to
    - Might be worth investing in stickers or some such for phase 4
      ground/space; I'd be happy to finance this
    - Problems with GNURadio came up a couple of times during the
      conference; Michelle's offer to help with this may be an excellent
      way to increase awareness


2 [2018-09-24 Mon]
==================

  - Intro from Artur and Manthos
    - "We need lots of people involved in open source and space -- and
      not only space engineers."
      - \o/ there's hope for me yet
    - Two open access journals, Software X and Hardware X (both from
      Elsevier :O) offering to publish papers from the workshops free of
      charge
    - Maybe 20% at this workshop were here last year
    - Mention of sdrmaker.space
      ([https://sdrmaker.space/2018/08/sdrmakerspace-initial/]),
      partnership between LibreSpace and ESA to fund work on using SDRs
      for satellite communications
  - Bruce on open source
    - On manufacturing cubesats for cheap: "Why use a fake satellite in
      your classroom? A university can afford a *real* one."
  - Formation flying talk
    - Calibration of telescopes very important -- they're sensitive
      enough that systematic effects are the biggest source of
      uncertainty.
    - There are natural sources that have well-known *intensities*, but
      that's not true of *polarization* -- and that's what they want to
      mention.
      - That's where the cubesat comes in
    - Used open source tools for design
      - OCDT: client/server; Concorde for concurrent design; ESA
        standard for workstation communication? ESA models for different
        submodules?
        - [https://ocdt.esa.int]: "OCDT is a client / server software
          package developed under a European Space Agency (ESA) contract
          to enable efficient multi-disciplinary concurrent engineering
          of space systems in the early life cycle phases." Avail only
          to people at institutions in ESA member states.
  - MM wave polarizatoin (Mansur Tisaev)
    - Another open source case study (OS tools used for design, antenna
      simulation)
  - Break
    - Artur: continuing conversation with ESA (ESAC?) director about
      open source. No, he won't require it, but can still prompt.
  - Cansat
    - Model rocket payload -- excellent introduction to working with
      cubesats
    - cansat.eu: ESA website
    - open-cosmos.org
  - Ilias from SatNOGS: pq9ish
    - Wasn't satisfied with RS485 bus in pq9, so designed with CANBus:
      gets to treat data like packets; mult-imaster message , message
      notification comes free; would be really hard to implement this on
      RS485 & would have to be done from scratch
    - used STM32 ARM chip; heritage from UPSat
    - Q: launch options to LEO? A: Piggyback on cubesat, or use cubesat
      as deployer
  - SatNOGS update
    - They are doing a lot of work to "close the loop" for telemetry
      from satellites: not only to collect raw radio signals, but to
      decode them to data frames and from there to telemetry
    - This includes beginning work on graphical display of satellite
      telemetry (dashboard showing temperature, battery levels, etc over
      time); still work in promise, but looks amazing
      - Based on Grafana for display, kaitai ([https://kaitai.io])
        parsing
      - This depends on knowing the data format for a given cubesat --
        this can be reverse engineered in a pinch, but immensely easier
        (and much more likely to happen) if the project actually
        publishes details
      - Q: what do you need from satellite operators to be able to
        decode the data frames? A: Publish encoding and data spec --
        otherwise we have to reverse engineer
  - TUDSat
    - We've had a lot of problems with GNURadio - lots of installaton
      probs, bugs, changes between versions, etc
    - Q to audience: what has your experience w/GNU radio been?
      Response (two people): Stick with GNURadio; some friction but once
      that's done everything is in one codebase.
  - MAGIC:
    - open source connection mainly sharing scientific data from
      instrument?
    - Talked to Dr. Chiara Palla, who made this presentation; she
      created the MAGIC instrument and helped integrate it into another
      team's cubesat
      - That integration took a lot of work: there were some things
        (software and hardware, IIUC) that were not well-specified, and
        a fair amount of iteration to get things sorted
      - I'm unsure if this is case for standardization, or for better
        comms between teams
  - ESA Summer of Code in Space: Red (moderator) is one of the
    organizers of this
    - didn't happen this year (timing? funding?)
    - goal is to have this not only in ESA but other places too
  - Python workshop
    - Focused on pros and cons of using Python, particularly for
      astronomy/space data
    - Included discussion of ease of use, which is a concern that
      extends beyond Python
      - Docker is a good solution, but you can't count on other people
        having it.
        - This was quite surprising to me; in current job/industry, if
          you don't know Docker it's expected you'll learn at least
          basic use of it quickly.  Another (welcome!) reminder that not
          everyone has the same experience/imperatives you do.


3 [2018-09-25 Tue]
==================

  - Conversation with Milenko Starik from TUDSat; asked for guidance re:
    troubleshooting unexpected performance problems with
    LimeSDR. Pointed him to Michelle, who was able to offer guidance
  - Conversation with Argentina Radio Club about their project to build
    up cubesat interest in their country, and about Phase 4 Ground
  - Team Anant
    - open source cubesat project from India
    - Using Zboard for POC, PetaLinux (prov. by vendor) for distro
    - Zboard too big for flight; wll use same SoC on final board
  - Poquet Cube - Nepal
    - Another vote for cansat for training
  - OpenMCT
    - NASA mission control dashboard; used by lightsail 2 among others
    - flexible enough to be used by *lots* of things
  - Ruediger Gad: use of non-space components
    - used message-oriented middleware (openwire, stomp) to translate
      between ie java programs used by esa and vr libraries written in
      latest hotness
    - looks like a very interesting way to do this kind of translation;
      good to keep in back pocket
  - Break
    - talked to Xabier Crespo Álvarez about idea of analyzing telemetry
      from SatNOGS DB to find signs of impending failure; should be good
      to use as first training set; volunteered to help with setting up
      pipeline, etc
  - Orekit
    - most cubesat projects don't need a lot of flight dynamics
      analysis; "as long as it does not fall...", and as long as you've
      got screen to display beautiful keplerian trajectory for VIPs
    - "clearly TLEs are not an option for high accuracy positioning"; i
      had no idea
  - Marcin Stolarski, hyper-sat.com
    - Had chance to talk with him afterward, so notes integrated here
    - New standard he's building to handle case when cubesats aren't big
      enough, which can happen more ofen than you think
    - new standard for larger-than-cubesat: 350mm x 350mm x (100-600)mm
    - what does this do to launch costs?
      - don't forget, launch cost will include PPOD as well -- so yes,
        more mass, but total cost ~ the same
      - not that much bigger (as far as volume goes); yes, will still
        fit on RocketLabs' Electron
      - a *lot* of engineering effort can go into miniaturizing
        instruments so that they'll fit into a cubesat; this is a
        standard that has more space, so you don't have to spend that
        time/money
      - aimed at startups; "here's 10 million, show me your proof of
        concept in a year."
    - why proprietary launch ring?
      - there were standard options but they're more expensive; will
        need diff adapters for diff rockets
    - about two years for docs; why?
      - work still in progress, heavy iteration. next step is to build
        test version, and will probably adjust standard when that
        happens (lessons learned); can email him for standards in
        meantime
  - Daina Bourquin, Harvard Library
    - talked to her about metadata, citations for software
    - tools:
      - zenudo: cern project to archive (and create DOI for) github repo
        via webhooks when you cut a rlease
      - codemeta
      - reprozip
      - software citation implementation working group
      - software presentation network
    - Her challenge: make it easy for teams to do the right thing re:
      archiving
    - why satnogs? because it's a challenging audience! if i can serve &
      make things easy for a dynamic community that does *not* have this
      in mind, then the rest is easy.
  - pc104 workshop/librecube:
    - organizer's intention was to keep this focused on certain pin
      arrangements in header; that didn't happen
    - problems with pc104:
      - how to make flatsat with pc104? have to make daughterboard; this
        is not how it will fly; assembly is a big part of testing how
        you fly, and can't do that & still have easy access to
        boards. switching to backplane would fix this
        - yes, would still have to test for insert cycles, thermal,
          vibration -- but this would be a great place to start.
      - know what else sucks about pc104? slow, annoying serial
        communications. ethernet would be great for this.
        - need higher data rates: 10mbit from an instrument, 2Gbit
          download (these are real examples); well beyond what pc104 can
          support.
      - pc104 takes up a lot of vertical room; going custom also allows
        you to save a lot of space.
      - what we have, has lasted us 10 years. we should be developing
        for *next* ten years, not optimizing a very old standard.
    - but pc104 is what people are using and selling, it's not
      obsolete. and physical support from header is an important
      benefit.
    - failure rate on cubesats. any ideas?
      - radios are a problem -- ask any ham why using power meter chips
        as alternative to AX.25 is a good thing (not sure i understood
        this point; Bruce was the one who made it, so it might be good
        to ask him)
      - also, i2c can lock bus -- and if you don't have good,
        well-tested watchdog, you have now just frozen your sat.
