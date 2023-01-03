# Motivation

At [Productsup](https://www.productsup.com/), we maintain a [Tech
Radar](https://radar.productsup.dev/) to help our engineering teams
align on technology choices. It is based on the [pioneering work
by ThoughtWorks](https://www.thoughtworks.com/radar).

This version is a modified version from [Yoyo Wallet](https://github.com/yoyowallet/tech-radar).

This repository contains the code to generate the visualization:
[`radar.js`](/docs/radar.js) (based on [d3.js v4](https://d3js.org)), and
was forked from work originally done by [Zalando](https://github.com/zalando/tech-radar).
Feel free to use and adapt it for your own purposes.

## How do I create a new version of the Techradar

1. Adjust or add technologies in our [Google Sheet](https://docs.google.com/spreadsheets/d/1Op2gILhJWK1YldR60xWBYMKxajSkHsy25DL_7y14HpU/edit?id=1Op2gILhJWK1YldR60xWBYMKxajSkHsy25DL_7y14HpU#gid=0) <br/>
**FYI:** Only the [Techradar board members](https://productsup.atlassian.net/wiki/spaces/EN/pages/1815380194/Tech+Radar#Who-is-part-of-the-Tech-Radar-board?) have write access to this sheet.
2. Create a new branch and a PR
3. Install dependencies with yarn (or npm) `docker-compose run --rm cli yarn`
4. Generate a new version by executing `docker-compose run --rm cli yarn generate` on the root of this project
5. Commit the changed files
6. Follow the review process in the PR template
7. Merge the PR
8. Create a new release in GitHub

**That's it!!**

## Usage

1. include `d3.js` and `radar.js`:

```html
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="http://productsupcom.github.io/tech-radar/release/radar-0.5.js"></script>
```

2. insert an empty `svg` tag:

```html
<svg id="radar"></svg>
```

3. configure the radar visualization:

```js
radar_visualization({
  svg_id: "radar",
  width: 1450,
  height: 1000,
  colors: {
    background: "#fff",
    grid: "#bbb",
    inactive: "#ddd"
  },
  title: "My Radar",
  quadrants: [
    { name: "Bottom Right" },
    { name: "Bottom Left" },
    { name: "Top Left" },
    { name: "Top Right" }
  ],
  rings: [
    { name: "INNER",  color: "#93c47d" },
    { name: "SECOND", color: "#b7e1cd" },
    { name: "THIRD",  color: "#fce8b2" },
    { name: "OUTER",  color: "#f4c7c3" }
  ],
  print_layout: true,
  entries: [
   {
      label: "Some Entry",
      quadrant: 3,          // 0,1,2,3 (counting clockwise, starting from bottom right)
      ring: 2,              // 0,1,2,3 (starting from inside)
      moved: -1             // -1 = moved out (triangle pointing down)
                            //  0 = not moved (circle)
                            //  1 = moved in  (triangle pointing up)
   },
    // ...
  ]
});
```

Entries are positioned automatically so that they don't overlap.

As a working example, you can check out `docs/index.html` &mdash; the source of our [public Tech
Radar](http://yoyowallet.github.io/tech-radar/).

## Local Development

1. install dependencies with yarn (or npm):

```
docker-compose run --rm cli yarn
```

2. start local dev server:

```
docker-compose run --rm --service-ports cli yarn start
```

3. your default browser should automatically open and show the url

```
http://localhost:3000/
```

4. update entries from Google Docs:

```
docker-compose run --rm cli yarn generate
```
