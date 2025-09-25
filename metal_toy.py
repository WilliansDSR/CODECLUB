#!/usr/bin/env python3
"""
Metal Toy: energy evolution with minimal instability (curvature != 0)
Run in 1 minute:
    python metal_toy.py --steps 300 --alpha 0.08 --beta 0.6 --gamma 0.02 --plot 0
Optional plot (saves PNG):
    python metal_toy.py --plot 1
"""
import argparse, math, random, time
import sys

def simulate(steps=300, dt=0.05, E0=1.2, alpha=0.08, beta=0.6, gamma=0.02, noise=0.0, seed=123):
    # dE/dt = -alpha*E + beta - gamma*E*E  (+ noise)
    # This has nonzero second derivative generically -> not globally linear.
    random.seed(seed)
    E = E0
    history = [E]
    for _ in range(steps):
        dE = -alpha*E + beta - gamma*(E*E)
        dE += noise*(random.random()-0.5)
        E += dt*dE
        history.append(E)
    return history

def curvature_discrete(y):
    # Discrete second difference as curvature proxy
    curv = []
    for i in range(1, len(y)-1):
        curv.append(y[i+1] - 2*y[i] + y[i-1])
    return curv

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", type=int, default=300)
    ap.add_argument("--dt", type=float, default=0.05)
    ap.add_argument("--E0", type=float, default=1.2)
    ap.add_argument("--alpha", type=float, default=0.08)
    ap.add_argument("--beta", type=float, default=0.6)
    ap.add_argument("--gamma", type=float, default=0.02)
    ap.add_argument("--noise", type=float, default=0.0)
    ap.add_argument("--plot", type=int, default=0)
    ap.add_argument("--seed", type=int, default=123)
    args = ap.parse_args()

    t0 = time.time()
    y = simulate(args.steps, args.dt, args.E0, args.alpha, args.beta, args.gamma, args.noise, args.seed)
    curv = curvature_discrete(y)

    # Metrics
    trend = "escape (up)" if y[-1] > y[0] else "decay (down)"
    nonzero_curv = any(abs(c) > 1e-9 for c in curv)
    print(f"[MetalToy] steps={args.steps} dt={args.dt}")
    print(f"[MetalToy] trend: {trend}")
    print(f"[MetalToy] has_nonzero_curvature: {nonzero_curv}")
    print(f"[MetalToy] first 5 energies: {y[:5]}")
    print(f"[MetalToy] last 5 energies:  {y[-5:]}")

    if args.plot:
        try:
            import matplotlib.pyplot as plt
            t = [i*args.dt for i in range(len(y))]
            plt.figure()
            plt.plot(t, y, label="E(t)")
            plt.xlabel("t")
            plt.ylabel("Energy")
            plt.title("Metal Toy: Energy evolution (nonlinear, nonzero curvature)")
            out = "metal_toy.png"
            plt.savefig(out, dpi=180, bbox_inches="tight")
            print(f"[MetalToy] plot saved to {out}")
        except Exception as e:
            print(f"[MetalToy] plotting failed: {e}", file=sys.stderr)

    print(f"[MetalToy] done in {time.time()-t0:.3f}s")

if __name__ == "__main__":
    main()
