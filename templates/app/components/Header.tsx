'use client';
import { Menu, Search, HelpCircle, Sparkles } from 'lucide-react';
import type { SVGProps } from 'react';

const BurgerExpandIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg viewBox="0 0 32 32" fill="currentColor" {...props}>
    <path d="M0 4.5A1.5 1.5 0 0 1 1.5 3h29a1.5 1.5 0 1 1 0 3h-29A1.5 1.5 0 0 1 0 4.5ZM30.5 15h-29a1.5 1.5 0 1 0 0 3h29a1.5 1.5 0 1 0 0-3Zm0 12h-29a1.5 1.5 0 1 0 0 3h29a1.5 1.5 0 1 0 0-3Z" />
  </svg>
);

const MagnifyerIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg viewBox="0 0 32 32" fill="currentColor" {...props}>
    <path d="M13.999 28c3.5 0 6.697-1.3 9.154-3.432l6.139 6.139a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414l-6.139-6.139A13.93 13.93 0 0 0 27.999 14c0-7.72-6.28-14-14-14s-14 6.28-14 14 6.28 14 14 14Zm0-26c6.617 0 12 5.383 12 12s-5.383 12-12 12-12-5.383-12-12 5.383-12 12-12Z" />
  </svg>
);

const QuestionMarkIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg viewBox="0 0 24 24" fill="currentColor" {...props}>
    <path d="M13.749 20a1.75 1.75 0 1 1-3.499.001A1.75 1.75 0 0 1 13.75 20Zm-1.75-18c-4.139 0-6 3-6 5.131V8a.5.5 0 0 0 .5.5h2a.5.5 0 0 0 .5-.5v-.869c0-.45.509-2.131 3-2.131 2.783 0 3 2.095 3 2.736 0 1.375-1.021 2.073-1.463 2.311-1.209.651-3.037 1.635-3.037 4.347V15.5a.5.5 0 0 0 .5.5h2a.5.5 0 0 0 .5-.5v-1.106c0-.835.276-1.068 1.461-1.705C16.863 11.665 18 9.813 18 7.737c0-2.763-1.878-5.737-6-5.737Z" />
  </svg>
);

const AiIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg viewBox="0 0 32 32" {...props}>
    <defs>
      <linearGradient gradientUnits="userSpaceOnUse" id="ai-gradient" x1="0%" x2="82%" y1="3.4%" y2="123%">
        <stop offset="0.27" stopColor="#be98f9" />
        <stop offset="0.83" stopColor="#ff8bde" />
      </linearGradient>
    </defs>
    <path
      d="M24.75 0h-1.5A5.25 5.25 0 0 1 18 5.25v1.5A5.25 5.25 0 0 1 23.25 12h1.5A5.25 5.25 0 0 1 30 6.75v-1.5A5.25 5.25 0 0 1 24.75 0ZM0 15c4.444 0 7 2.5 7 7h2c0-4.5 2.5-7 7-7v-2c-4.5 0-7-2.5-7-7H7c0 4.5-2.5 7-7 7v2Zm20.75 17A5.25 5.25 0 0 1 26 26.75v-1.5A5.25 5.25 0 0 1 20.75 20h-1.5A5.25 5.25 0 0 1 14 25.25v1.5A5.25 5.25 0 0 1 19.25 32h1.5Z"
      fill="url(#ai-gradient)"
    />
  </svg>
);

export default function Header() {
  return (
    <header className="flex h-12 w-full items-center justify-between bg-[#27272a] px-2 text-zinc-300">
      <div className="flex items-center gap-2">
        <button className="rounded p-1.5 hover:bg-zinc-700">
          <BurgerExpandIcon className="h-5 w-5" />
        </button>
        <img
          src="https://d3ki9tyy5l5ruj.cloudfront.net/obj/ca0c1e32771e1bdf0f307099826f5994e3dc59e4/Asana-Logo-Horizontal-Coral-White.svg"
          alt="Asana logo"
          className="h-4"
        />
      </div>

      <div className="flex-1 px-8">
        <div className="mx-auto flex w-full max-w-2xl cursor-pointer items-center rounded-md bg-[#3f3f46] px-3 py-1.5 text-zinc-400">
          <MagnifyerIcon className="h-5 w-5" />
          <span className="ml-2 text-sm">Search</span>
        </div>
      </div>

      <div className="flex items-center gap-2">
        <button className="rounded p-1.5 hover:bg-zinc-700">
          <QuestionMarkIcon className="h-5 w-5" />
        </button>
        <button className="rounded p-1.5 hover:bg-zinc-700">
          <AiIcon className="h-5 w-5" />
        </button>
      </div>
    </header>
  );
}