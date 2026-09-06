/**
 * Photo provenance and credit.
 *
 * Every image on the site is listed here with where it came from and what is
 * known about rights. This exists because the photo audit turned up two real
 * problems that would otherwise have shipped:
 *
 *   1. One archive image showed rowers in MIT kit (an alumni post), not CRLS.
 *      It has been removed rather than used as if it were the team.
 *   2. The strongest image in the archive is a row2k frame. row2k is a
 *      commercial rowing-photography outfit and its images are licensed, not
 *      free to reuse. It is credited here and flagged for clearance.
 *
 * `clearance` values:
 *   'team'      — posted by the team on its own account, credit the team
 *   'licensed'  — cleared for use, note the licence
 *   'NEEDS_CLEARANCE' — do not publish until permission is obtained
 */

export const PHOTOS = {
  'DOXG__QDz1p.jpg': {
    caption: 'Novice squad at the Cambridge Boat Club, oars up.',
    alt: 'Fourteen novice rowers and a coach standing in a line on gravel at dusk, each holding a single long black oar horizontally across the frame, the boathouse lit behind them',
    credit: '@crlscrew',
    source: 'https://www.instagram.com/crlscrew/',
    clearance: 'team',
  },
  'DY-7vl_HNW6.jpg': {
    caption: 'Boys four at the dock with New England medals — the third and fourth in program history.',
    alt: 'Four rowers seated in their black racing shell at the dock, grinning and holding up bronze medals on blue ribbons',
    credit: 'row2k',
    source: 'https://www.instagram.com/crlscrew/',
    clearance: 'NEEDS_CLEARANCE',
    note: 'row2k licenses its race photography. Obtain permission or replace before publishing.',
  },
  'DYuDYwgnI_0.jpg': {
    caption: 'Girls four with New England silver.',
    alt: 'Five athletes shoulder to shoulder at a regatta site, each wearing a silver medal on a blue lanyard',
    credit: '@crlscrew',
    source: 'https://www.instagram.com/crlscrew/',
    clearance: 'team',
  },
  'DYTRVUeySLb.jpg': {
    caption: 'Seniors, in the colours of the programs they are rowing for next.',
    alt: 'About twelve senior athletes in a line on a wooden dock, each wearing the sweatshirt of the college they committed to',
    credit: '@crlscrew',
    source: 'https://www.instagram.com/crlscrew/',
    clearance: 'team',
  },
  'DYccfKfy-U7.jpg': {
    caption: 'The squad at the national championship.',
    alt: 'Twelve people arm in arm on grass in front of a white USRowing banner, athletes in black CRLS unisuits wearing medals',
    credit: '@crlscrew',
    source: 'https://www.instagram.com/crlscrew/',
    clearance: 'team',
  },
  'DZc7FyzS00e.jpg': {
    caption: 'Nathan Benderson Park, Sarasota — Youth Nationals.',
    alt: 'Six athletes posed at the Nathan Benderson Park monument sign at the USRowing Youth National Championships',
    credit: '@crlscrew',
    source: 'https://www.instagram.com/crlscrew/',
    clearance: 'team',
  },
  'DOjXd1Wj9BF.jpg': {
    caption: 'The boat bay.',
    alt: 'Racing shells racked inside the Cambridge Boat Club boat bay',
    credit: '@crlscrew',
    source: 'https://www.instagram.com/crlscrew/',
    clearance: 'team',
  },
};

/** Images that must not be published until rights are cleared. */
export const BLOCKED = Object.entries(PHOTOS)
  .filter(([, p]) => p.clearance === 'NEEDS_CLEARANCE')
  .map(([file]) => file);
