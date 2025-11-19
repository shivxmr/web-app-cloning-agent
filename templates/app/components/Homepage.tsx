'use client';
import { useState } from 'react';
import { MoreHorizontal, Lock, Plus, Circle, ChevronDown, Check, Users, Play, Book, Rocket } from 'lucide-react';

const CustomizeIcon = () => (
  <svg width="16" height="16" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg" className="mr-1.5">
    <path d="M0.75 3.75H2.25V0.75H0.75V3.75Z" fill="#636366"/>
    <path d="M0.75 11.25H2.25V5.25H0.75V11.25Z" fill="#636366"/>
    <path d="M5.25 3H3.75V0.75H5.25V3Z" fill="#636366"/>
    <path d="M3.75 11.25H5.25V4.5H3.75V11.25Z" fill="#636366"/>
    <path d="M9.75 5.25H11.25V0.75H9.75V5.25Z" fill="#636366"/>
    <path d="M11.25 6.75H9.75V11.25H11.25V6.75Z" fill="#636366"/>
    <path d="M6.75 6H8.25V0.75H6.75V6Z" fill="#636366"/>
    <path d="M8.25 7.5H6.75V11.25H8.25V7.5Z" fill="#636366"/>
  </svg>
);

const SmallSquircleIcon = () => (
  <svg aria-hidden="true" className="h-3 w-3 text-[#62d2b1]" focusable="false" viewBox="0 0 24 24">
    <path d="M10.4,4h3.2c2.2,0,3,0.2,3.9,0.7c0.8,0.4,1.5,1.1,1.9,1.9s0.7,1.6,0.7,3.9v3.2c0,2.2-0.2,3-0.7,3.9c-0.4,0.8-1.1,1.5-1.9,1.9s-1.6,0.7-3.9,0.7h-3.2c-2.2,0-3-0.2-3.9-0.7c-0.8-0.4-1.5-1.1-1.9-1.9c-0.4-1-0.6-1.8-0.6-4v-3.2c0-2.2,0.2-3,0.7-3.9C5.1,5.7,5.8,5,6.6,4.6C7.4,4.2,8.2,4,10.4,4z" fill="currentColor"></path>
  </svg>
);

const GetStartedRocketIllustration = () => (
  <svg className="h-24 w-24 text-gray-700" viewBox="0 0 200 200">
    <path className="stroke-current fill-[#FCEEED]" d="M191.575 189.318a20.94 20.94 0 0 0-8.445-15.028c-1.282-10.351-10.098-18.37-20.8-18.37-9.781 0-17.993 6.697-20.31 15.756a21 21 0 0 0-6.118 3.752c-16.795-12.207-28.225-31.447-29.853-53.608H93.694c-1.46 19.933-10.86 37.506-24.958 49.717a20.8 20.8 0 0 0-5.92-1.282c-2.773-8.331-10.628-14.34-19.89-14.34-11.578 0-20.963 9.385-20.963 20.963q.001.714.055 1.411a21.04 21.04 0 0 0-11.821 11.019 20.85 20.85 0 0 0-1.836 9.672h181.793a20.9 20.9 0 0 0 1.515-7.816c0-.624-.035-1.242-.089-1.856zM147.56 103.668H52.332v7.098h95.228z"></path>
    <path className="stroke-current fill-[#FCEEED]" d="M85.333 110.925h29.334v8.806a5.945 5.945 0 0 1-5.94 5.94H91.273a5.945 5.945 0 0 1-5.94-5.94z"></path>
    <path className="stroke-current fill-[#F06A6A]" d="M70.676 37.665h-.005c-5.919 0-10.717 4.798-10.717 10.717v44.564c0 5.92 4.798 10.717 10.717 10.717h.005c5.919 0 10.717-4.798 10.717-10.717V48.382c0-5.92-4.798-10.717-10.717-10.717Z"></path>
    <path className="stroke-current fill-white" d="M81.66 52.782c0 8.118-5.5 15.207-13.36 17.221l-2.603.668a17.77 17.77 0 0 0-13.36 17.221v15.781h47.559V52.787h-18.23z"></path>
    <path className="stroke-current fill-[#F06A6A]" d="M129.22 103.668h.005c5.919 0 10.717-4.798 10.717-10.717V48.386c0-5.918-4.798-10.716-10.717-10.716h-.005c-5.919 0-10.717 4.798-10.717 10.716v44.565c0 5.919 4.798 10.717 10.717 10.717Z"></path>
    <path className="stroke-current fill-white" d="M118.231 52.782a17.78 17.78 0 0 0 13.36 17.221l2.604.668a17.77 17.77 0 0 1 13.36 17.221v15.781h-47.56V52.787h18.231z"></path>
    <path className="stroke-[#F06A6A]" d="M59.955 118.295v12.999M66.617 118.295v5.668M139.501 118.295v12.999M132.843 118.295v5.668"></path>
    <path className="stroke-current fill-white" d="M118.176 39.026A48.6 48.6 0 0 0 105.643 6.46a48.6 48.6 0 0 0-5.623-5.316L99.842 1a48.5 48.5 0 0 0-5.802 5.455A48.6 48.6 0 0 0 81.507 39.03v79.329h36.669z"></path>
    <path className="stroke-current fill-[#FCEEED]" d="M100 27.285c2.797 0 5.702 1.48 7.781 2.826h3.218v-.46c0-3.673-4.925-6.648-11-6.648-6.073 0-10.998 2.975-10.998 6.648v.46h3.079c2.109-1.346 5.128-2.826 7.92-2.826Z"></path>
    <path className="stroke-current fill-white" d="M99.842 44.15c-1.238 0-2.253 1.365-2.287 3.078l-1.381 71.127h7.331l-1.381-71.127c-.035-1.713-1.05-3.079-2.287-3.079z"></path>
  </svg>
);

export default function Homepage() {
  const [activeTab, setActiveTab] = useState('Upcoming');
  const tabs = ['Upcoming', 'Overdue', 'Completed'];
  const tasks = [
    { id: 1, name: '1. Frontend', project: 'clooney', dueDate: 'Nov 15 – Today' },
    { id: 2, name: '2. Backend', project: 'clooney', dueDate: 'Nov 17 – 19' },
  ];
  const learningCards = [
    {
      title: "Getting started",
      description: "Learn the basics and see how Asana helps you get work done.",
      duration: "3 min",
      type: "video",
      Icon: GetStartedRocketIllustration,
    },
    {
      title: "Manage student organizations",
      description: "Learn how to organize meetings, events, and projects in Asana.",
      duration: "5 min read",
      type: "read",
      Icon: () => <Rocket className="h-24 w-24 text-gray-400" />,
    },
    {
      title: "Build a product roadmap",
      description: "See how to prioritize and plan your roadmap in Asana.",
      duration: "10 min read",
      type: "read",
      Icon: () => <Rocket className="h-24 w-24 text-gray-400" />,
    },
  ];

  return (
    <div className="min-h-screen bg-[#F9F8F7] bg-[url('https://d3ki9tyy5l5ruj.cloudfront.net/obj/4f90741232dcb86dc90dc67a6f8e834e404ce515/Oat_background.png')] bg-cover">
      <main className="p-8">
        <header className="flex justify-between items-start mb-6">
          <div>
            <p className="text-sm font-medium text-gray-500">Tuesday, November 18</p>
            <h1 className="text-4xl text-gray-800 mt-1">Good morning, Shivam</h1>
          </div>
          <div className="flex items-center space-x-3">
            <button className="flex items-center bg-white border border-gray-200/80 rounded-md px-3 py-1.5 text-sm text-gray-700 shadow-sm hover:bg-gray-50">
              My week
              <ChevronDown className="h-4 w-4 ml-1 text-gray-500" />
            </button>
            <div className="flex items-center space-x-4 text-sm text-gray-600">
              <div className="flex items-center space-x-1">
                <Check className="h-4 w-4" />
                <span>0 tasks completed</span>
              </div>
              <div className="flex items-center space-x-1">
                <Users className="h-4 w-4" />
                <span>0 collaborators</span>
              </div>
            </div>
            <button className="flex items-center bg-white border border-gray-200/80 rounded-md px-3 py-1.5 text-sm text-gray-700 shadow-sm hover:bg-gray-50">
              <CustomizeIcon />
              Customize
            </button>
          </div>
        </header>

        <div className="space-y-6">
          <div className="bg-white rounded-2xl border border-gray-200/80 shadow-sm p-6 relative">
            <button className="absolute top-4 right-4 text-gray-500 hover:bg-gray-100 rounded-full p-1">
              <MoreHorizontal className="h-5 w-5" />
            </button>
            <div className="flex items-start space-x-4">
              <div className="w-16 h-16 rounded-full bg-[#F8C56B] flex-shrink-0 flex items-center justify-center">
                <span className="text-2xl font-medium text-[#8C6416]">SR</span>
              </div>
              <div className="flex-grow">
                <div className="flex items-center space-x-2">
                  <h4 className="text-xl font-medium text-gray-900">My tasks</h4>
                  <Lock className="h-4 w-4 text-gray-500" />
                </div>
                <div className="mt-2 border-b border-gray-200">
                  <nav className="-mb-px flex space-x-6" aria-label="Tabs">
                    {tabs.map((tab) => (
                      <button
                        key={tab}
                        onClick={() => setActiveTab(tab)}
                        className={`whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm ${
                          activeTab === tab
                            ? 'border-gray-800 text-gray-900'
                            : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                        }`}
                      >
                        {tab}
                      </button>
                    ))}
                  </nav>
                </div>
              </div>
            </div>
            <div className="pl-20 mt-4">
              <button className="flex items-center text-sm text-gray-600 hover:bg-gray-100 rounded-md px-2 py-1">
                <Plus className="h-4 w-4 mr-2" />
                Create task
              </button>
              <div className="mt-2">
                {tasks.map((task) => (
                  <div key={task.id} className="flex items-center justify-between py-2.5 border-b border-gray-100 last:border-b-0">
                    <div className="flex items-center space-x-3">
                      <Circle className="h-5 w-5 text-gray-400" />
                      <span className="text-sm text-gray-800">{task.name}</span>
                    </div>
                    <div className="flex items-center space-x-4">
                      <div className="flex items-center space-x-1.5 bg-gray-100 rounded-full px-2 py-0.5">
                        <SmallSquircleIcon />
                        <span className="text-xs text-gray-700">{task.project}</span>
                      </div>
                      <span className="text-sm text-gray-500">
                        {task.dueDate.split('–')[0]}–
                        <span className={task.dueDate.includes('Today') ? 'text-green-600' : ''}>
                          {task.dueDate.split('–')[1]}
                        </span>
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="bg-white rounded-2xl border border-gray-200/80 shadow-sm p-6 relative">
            <div className="flex justify-between items-center">
              <h4 className="text-xl font-medium text-gray-900">Learn Asana</h4>
              <button className="text-gray-500 hover:bg-gray-100 rounded-full p-1">
                <MoreHorizontal className="h-5 w-5" />
              </button>
            </div>
            <div className="mt-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
              {learningCards.map((card, index) => (
                <div key={index} className="bg-[#fdecec] rounded-lg p-4 flex flex-col justify-between h-[280px] relative group cursor-pointer">
                  <div className="absolute top-4 right-4 bg-[#f06a6a] text-white text-xs font-medium px-2.5 py-1 rounded-full flex items-center space-x-1">
                    {card.type === 'video' ? <Play className="h-3 w-3" /> : <Book className="h-3 w-3" />}
                    <span>{card.duration}</span>
                  </div>
                  <div className="flex-grow flex items-center justify-center">
                    <card.Icon />
                  </div>
                  <div className="mt-auto">
                    <h5 className="font-medium text-gray-900">{card.title}</h5>
                    <p className="text-sm text-gray-600 mt-1 line-clamp-2">{card.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}