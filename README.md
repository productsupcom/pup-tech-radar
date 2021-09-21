# Motivation

At [Productsup](https://www.productsup.com/), we maintain a [public Tech
Radar](http://productsup.github.io/tech-radar/) to help our engineering teams
align on technology choices. Is is based on the [pioneering work
by ThoughtWorks](https://www.thoughtworks.com/radar).

This version is a modified version from [Yoyo Wallet](https://github.com/yoyowallet/tech-radar).

This repository contains the code to generate the visualization:
[`radar.js`](/docs/radar.js) (based on [d3.js v4](https://d3js.org)), and
was forked from work originally done by [Zalando](https://github.com/zalando/tech-radar).
Feel free to use and adapt it for your own purposes.

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
yarn
```

2. start local dev server:

```
yarn start
```

3. your default browser should automatically open and show the url

```
http://localhost:3000/
```

4. update entries from Google Docs:

```
yarn generate
```
