#!/usr/bin/env python3
"""
AI Toy: multiplicative iteration showing closure to zero (or escape)
Run in 1 minute:
    python ai_toy.py --lam 0.98 --steps 500 --x0 1.0
Try escape:
    python ai_toy.py --lam 1.02 --steps 200 --x0 0.2
"""
import argparse, random, time

def iterate(lam=0.98, steps=500, x0=1.0, noise=0.0, seed=42):
    random.seed(seed)
    x = x0
    seq = [x]
    for _ in range(steps):
        # multiplicative contraction/expansion + tiny noise
        x = lam * x + noise*(random.random()-0.5)
        seq.append(x)
    return seq

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lam", type=float, default=0.98)
    ap.add_argument("--steps", type=int, default=500)
    ap.add_argument("--x0", type=float, default=1.0)
    ap.add_argument("--noise", type=float, default=0.0)
    ap.add_argument("--plot", type=int, default=0)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    t0 = time.time()
    seq = iterate(args.lam, args.steps, args.x0, args.noise, args.seed)
    behavior = "closure_to_zero" if abs(seq[-1]) < abs(seq[0]) and args.lam < 1.0 else "escape_or_neutral"
    print(f"[AIToy] lam={args.lam} steps={args.steps} x0={args.x0}")
    print(f"[AIToy] behavior: {behavior}")
    print(f"[AIToy] first 5: {seq[:5]}")
    print(f"[AIToy] last 5:  {seq[-5:]}")

    if args.plot:
        try:
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot(range(len(seq)), seq, label="x_n")
            plt.xlabel("n")
            plt.ylabel("x")
            plt.title("AI Toy: multiplicative iteration (closure vs escape)")
            out = "ai_toy.png"
            plt.savefig(out, dpi=180, bbox_inches="tight")
            print(f"[AIToy] plot saved to {out}")
        except Exception as e:
            print(f"[AIToy] plotting failed: {e}")

    print(f"[AIToy] done in {time.time()-t0:.3f}s")

if __name__ == "__main__":
    main()
