# gramps-online
A simple online version of Gramps

## Project vision
This project aims to produce a platform for collaborating on a shared genealogy network/graph. It should allow many people to edit the tree and keep track of changes.

The genealogy data should be made visible via intuitive and interactive graphical representations, to facilitate human understanding of our heritage.

The data produced through this collaborative process should be publicly accessible, part of our commonwealth, while respecting privacy of living persons.

## Design principles
The following principles guide decisions for design and development of this project.

- Main Prnciples:
  - Data privacy: possibility of granting permission for information in granular form (by person, or content relating to the person: specific events, notes,...): public access, authorized followers of a specific item, authorized followers, groups, all followers. Implementing solid should be taken into account.
  - Data sovereignty: federative model for servers/nodes, as in Fediverse. Implementing Solid should be taken into account.
  - Usability: it may be good to sacrifice some flexibility, so that end-users have an easy time
  - Pythonic code: e.g. follow the [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
 - Other Principles:
   - Well documented: follow well-documented Django conventions
