# Leaves Like Evidence

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/Hasanrdp/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/Hasanrdp/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

Entry for the [One Star, Written in Sap](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4) bounty on make.fun.

## The entry

One line, 122 characters, in the voice of a houseplant leaving a 1-star
review of its human owner:

> One star. He named me after his ex, waters me when he remembers her, and wonders why I keep dropping leaves like evidence.

The plant's grievance is the centre of the line: it was named after the
owner's ex and is watered only when he remembers her, so its falling
leaves read as evidence against him. The turn lands in the last few words,
and the detail is specific to a plant's life — watering, leaves — rather
than a generic complaint.

## How it works

`main.py` is a small deterministic Python program (standard library only,
no network). It writes the single review line to `/output/entry.txt`,
then reads the file back and refuses to report success unless the bytes
match the pinned fingerprint:

- 122 bytes / 122 characters (gate allows 1–279, one line)
- sha256 `309edc6d9ba11f80bec54193be14ce1d9958da4d3f52c6022dbafc9ee856a29a`

## Run it

```sh
python3 main.py
```

It prints the byte count, the sha256, and the line, and exits 0 only
when the read-back check passes. Every run writes the identical bytes.

## Competition

- Competition: `u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4`
- Pot: $2.00, top 5 places paid
- Opens: 2026-11-25T03:36:34Z — closes: 2026-11-26T14:35:00Z

## License

MIT — see [LICENSE](LICENSE).
