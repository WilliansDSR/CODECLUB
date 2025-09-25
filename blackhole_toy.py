#!/usr/bin/env python3
"""
Black Hole Toy: finite proper-time collapse via mass decay m'(tau) = -k * m^p with p>1
Analytic extinction time: T = m0^(1-p) / (k*(p-1))  (finite for p>1).
Run in 1 minute:
    python blackhole_toy.py --m0 1.0 --k 0.8 --p 1.5 --dt 0.001
Optional plot:
    python blackhole_toy.py --plot 1
"""
import argparse, math, time, sys

def simulate(m0=1.0, k=0.8, p=1.5, dt=1e-3, max_steps=200000):
    m = m0
    m_hist = [m]
    tau = 0.0
    for i in range(max_steps):
        dm = -k * (m**p)
        m = max(0.0, m + dt*dm)
        tau += dt
        m_hist.append(m)
        if m <= 1e-8:
            break
    return tau, m_hist

def extinction_time_analytic(m0=1.0, k=0.8, p=1.5):
    if p <= 1.0:
        return math.inf
    return (m0**(1.0-p)) / (k*(p-1.0))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m0", type=float, default=1.0)
    ap.add_argument("--k", type=float, default=0.8)
    ap.add_argument("--p", type=float, default=1.5)
    ap.add_argument("--dt", type=float, default=1e-3)
    ap.add_argument("--max_steps", type=int, default=200000)
    ap.add_argument("--plot", type=int, default=0)
    args = ap.parse_args()

    t0 = time.time()
    Tau_num, m_hist = simulate(args.m0, args.k, args.p, args.dt, args.max_steps)
    Tau_ana = extinction_time_analytic(args.m0, args.k, args.p)

    print(f"[BHToy] m0={args.m0} k={args.k} p={args.p} dt={args.dt}")
    print(f"[BHToy] numerical proper time to ~zero: {Tau_num:.6f}")
    print(f"[BHToy] analytic extinction time (finite if p>1): {Tau_ana:.6f}")
    print(f"[BHToy] first 5 masses: {m_hist[:5]}")
    print(f"[BHToy] last 5 masses:  {m_hist[-5:]}")

    if args.plot:
        try:
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot(range(len(m_hist)), m_hist, label="m(τ)")
            plt.xlabel("step")
            plt.ylabel("mass")
            plt.title("Black Hole Toy: finite-time mass decay (p>1)")
            out = "blackhole_toy.png"
            plt.savefig(out, dpi=180, bbox_inches="tight")
            print(f"[BHToy] plot saved to {out}")
        except Exception as e:
            print(f"[BHToy] plotting failed: {e}", file=sys.stderr)

    print(f"[BHToy] done in {time.time()-t0:.3f}s")

if __name__ == "__main__":
    main()
