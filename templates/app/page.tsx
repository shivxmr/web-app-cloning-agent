
'use client';

import React from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Homepage from './components/Homepage';


export default function Home() {
  return (
    <main className="flex h-screen bg-white text-gray-900">
      <aside className="w-64 h-full flex-shrink-0 bg-[#25282F]"><Sidebar /></aside>

      <div className="flex-1 flex flex-col h-full overflow-auto">
        <header className="sticky top-0 z-10"><Header /></header>

        <div className="flex-1 flex flex-col">
          <Homepage />
        </div>
      </div>
    </main>
  );
}
