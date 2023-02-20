---
sidebar_position: 1
---

# Getting Started

Let's discover **[starknet-devnet](https://github.com/Shard-Labs/starknet-devnet)**.
:::danger Take care

## ⚠️ Disclaimer ⚠️

:::

- Devnet should not be used as a replacement for Alpha testnet. After testing on Devnet, be sure to test on testnet (alpha-goerli)!
- Specifying a block by its hash/number is not supported for state querying. You can only choose between the pending or the latest block.
- Sending transactions with max_fee set to 0 is supported (not supported on alpha-mainnet or alpha-goerli).
- Devnet is currently being adapted to StarkNet and Cairo v0.10.0, if you spot any issues, please [report them](https://github.com/Shard-Labs/starknet-devnet/issues/new/choose).

## Requirements

Works with Python versions >=3.8 and <3.10.

On Ubuntu/Debian, first run:

```bash
$ sudo apt install -y libgmp3-dev
```

On Mac, you can use `brew`:

```bash
$ brew install gmp
```

## Install

```bash
$ pip install starknet-devnet
```

## Run

```
$ starknet-devnet
```

For more running possibilities, see [this](https://shard-labs.github.io/starknet-devnet/docs/guide/run).

### Windows installation

Follow this guide: https://www.spaceshard.io/blog/starknet-devnet-windows-tutorial
