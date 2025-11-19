'use client';
import React, { useState } from 'react';
import { Home, CheckCircle2, FolderKanban, Briefcase, ChevronDown, MoreHorizontal, Plus, Mail, Building } from 'lucide-react';

const CheckCircleFullIcon = (props) => (
  <svg viewBox="0 0 32 32" fill="currentColor" {...props}>
    <path d="M16,0C7.2,0,0,7.2,0,16s7.2,16,16,16s16-7.2,16-16S24.8,0,16,0z M23.3,13.3L14,22.6c-0.3,0.3-0.7,0.4-1.1,0.4s-0.8-0.1-1.1-0.4L8,18.8c-0.6-0.6-0.6-1.5,0-2.1s1.5-0.6,2.1,0l2.8,2.8l8.3-8.3c0.6-0.6,1.5-0.6,2.1,0S23.9,12.7,23.3,13.3z" />
  </svg>
);

const GoalSimpleIcon = (props) => (
  <svg viewBox="0 0 32 32" fill="currentColor" {...props}>
    <path d="M19.533 3.417A4.208 4.208 0 0 0 15.998 1.5a4.204 4.204 0 0 0-3.534 1.916L.694 21.443a4.186 4.186 0 0 0-.179 4.342A4.166 4.166 0 0 0 4.228 28h23.54a4.166 4.166 0 0 0 3.712-2.215 4.184 4.184 0 0 0-.179-4.342L19.532 3.416l.001.001Zm10.188 21.417a2.193 2.193 0 0 1-1.954 1.167H4.228a2.192 2.192 0 0 1-1.954-1.167 2.217 2.217 0 0 1 .094-2.296L14.14 4.51A2.183 2.183 0 0 1 16 3.501c.762 0 1.44.368 1.86 1.01l11.77 18.027c.456.701.49 1.559.092 2.296Z" />
  </svg>
);

const WorkflowIcon = (props) => (
  <svg viewBox="0 0 32 32" fill="currentColor" {...props}>
    <path d="M23,12h4c1.65,0,3-1.35,3-3V5c0-1.65-1.35-3-3-3h-4c-1.65,0-3,1.35-3,3v1h-7.6C11.93,3.44,9.69,1.5,7,1.5 C3.97,1.5,1.5,3.97,1.5,7c0,2.69,1.94,4.93,4.5,5.4V20H5c-1.65,0-3,1.35-3,3v4c0,1.65,1.35,3,3,3h4c1.65,0,3-1.35,3-3v-1h14.6 l-3.31,3.31c-0.39,0.39-0.39,1.02,0,1.41c0.2,0.2,0.45,0.29,0.71,0.29s0.51-0.1,0.71-0.29l5-5c0.2-0.2,0.29-0.46,0.29-0.71 c0,0,0,0,0-0.01c0-0.3-0.14-0.56-0.34-0.74l-4.97-4.97c-0.39-0.39-1.02-0.39-1.41,0s-0.39,1.02,0,1.41L26.57,24H12v-1 c0-1.65-1.35-3-3-3H8v-7.6c2.23-0.41,3.99-2.17,4.4-4.4H20v1C20,10.65,21.35,12,23,12z M22,5c0-0.55,0.45-1,1-1h4c0.55,0,1,0.45,1,1 v4c0,0.55-0.45,1-1,1h-4c-0.55,0-1-0.45-1-1V5z M9,22c0.55,0,1,0.45,1,1v4c0,0.55-0.45,1-1,1H5c-0.55,0-1-0.45-1-1v-4 c0-0.55,0.45-1,1-1H9z M7,10.5c-1.93,0-3.5-1.57-3.5-3.5S5.07,3.5,7,3.5s3.5,1.57,3.5,3.5S8.93,10.5,7,10.5z" />
  </svg>
);

const BellNotificationIcon = (props) => (
  <svg viewBox="0 0 32 32" {...props}>
    <path fill="#f54746" d="M26 12C29.3137 12 32 9.31371 32 6C32 2.68629 29.3137 0 26 0C22.6863 0 20 2.68629 20 6C20 9.31371 22.6863 12 26 12Z"></path>
    <path fill="currentColor" d="M19.733 28.0001H20.896C19.963 29.8171 18.081 31.0001 16 31.0001C13.919 31.0001 12.037 29.8171 11.104 28.0001H19.733ZM29.97 20.6351C28.718 19.5231 28 17.9241 28 16.2491V15.0001C28 14.4481 27.552 14.0001 27 14.0001C26.448 14.0001 26 14.4481 26 15.0001V16.2491C26 18.4951 26.962 20.6381 28.641 22.1301C29.008 22.4561 29.103 22.9791 28.88 23.4331C28.713 23.7721 28.298 24.0001 27.85 24.0001H4.15101C3.70201 24.0001 3.28801 23.7721 3.12101 23.4321C2.89701 22.9791 2.99301 22.4551 3.36001 22.1301C5.03801 20.6381 6.00101 18.4951 6.00101 16.2491V12.0001C6.00101 9.29407 7.06401 6.76007 8.99501 4.86407C10.926 2.96807 13.484 1.94307 16.189 2.00207C16.89 2.01407 17.589 2.10407 18.266 2.26807C18.802 2.39607 19.343 2.06807 19.473 1.53107C19.602 0.99407 19.273 0.45407 18.736 0.32407C17.917 0.12607 17.072 0.0180698 16.225 0.00306978C12.961 -0.0489302 9.91001 1.16407 7.59401 3.43807C5.27701 5.71307 4.00101 8.75407 4.00101 12.0011V16.2501C4.00101 17.9251 3.28301 19.5231 2.03101 20.6361C0.984005 21.5681 0.701006 23.0471 1.32701 24.3181C1.83101 25.3411 2.94001 26.0021 4.15101 26.0021H27.849C29.06 26.0021 30.169 25.3411 30.673 24.3191C31.299 23.0481 31.017 21.5691 29.969 20.6371L29.97 20.6351Z"></path>
  </svg>
);

export default function Sidebar() {
  const [isWorkExpanded, setIsWorkExpanded] = useState(true);
  const projectName = 'clooney';

  return (
    <div className="flex h-screen font-sans">
      <div className="bg-[#151b26] w-[72px] flex flex-col justify-between items-center py-4">
        <div className="flex flex-col items-center space-y-2">
          <ModeButton icon={<CheckCircleFullIcon className="w-8 h-8" />} label="Work" active />
          <ModeButton icon={<GoalSimpleIcon className="w-8 h-8" />} label="Plan" />
          <ModeButton icon={<WorkflowIcon className="w-8 h-8" />} label="Workflow" />
          <ModeButton icon={<Building className="w-8 h-8" />} label="Company" />
        </div>
        <div className="flex flex-col items-center space-y-4">
          <button className="w-10 h-10 bg-red-500 rounded-full flex items-center justify-center text-white">
            <Plus size={20} />
          </button>
          <button className="w-10 h-10 flex items-center justify-center text-gray-400 hover:text-white">
            <Mail size={24} />
          </button>
          <button className="w-10 h-10 bg-[#f8c173] rounded-full flex items-center justify-center text-black font-bold text-sm">
            SR
          </button>
        </div>
      </div>

      <div className="bg-[#212734] w-[240px] flex flex-col">
        <div className="flex-grow pt-4 px-2 overflow-y-auto">
          <nav className="flex flex-col space-y-1">
            <NavLink icon={<Home size={20} />} label="Home" active />
            <NavLink icon={<BellNotificationIcon className="w-5 h-5" />} label="Inbox" />
          </nav>

          <hr className="border-t border-[#3a3f4a] my-3" />

          <nav className="flex flex-col space-y-1">
            <NavLink icon={<CheckCircle2 size={20} />} label="My tasks" />
            <div className="h-2"></div>
            <NavLink icon={<FolderKanban size={20} />} label="Projects" />
            <NavLink icon={<Briefcase size={20} />} label="Portfolios" />
          </nav>

          <div className="mt-4">
            <div className="flex items-center justify-between px-2 py-1 text-gray-100">
              <button onClick={() => setIsWorkExpanded(!isWorkExpanded)} className="flex items-center space-x-2 text-sm w-full">
                <ChevronDown size={16} className={`transition-transform ${isWorkExpanded ? 'rotate-0' : '-rotate-90'}`} />
                <span className="font-semibold">Work</span>
              </button>
              <div className="flex items-center space-x-1">
                <button className="text-gray-400 hover:text-white p-1 rounded"><MoreHorizontal size={16} /></button>
                <button className="text-gray-400 hover:text-white p-1 rounded"><Plus size={16} /></button>
              </div>
            </div>
            {isWorkExpanded && (
              <div className="mt-1">
                <a href="#" className="flex items-center space-x-3 px-2 py-1.5 rounded-md text-gray-200 hover:bg-[#3a3f4a]">
                  <div className="w-5 h-5 bg-[#4dd0e1] rounded-md"></div>
                  <span className="text-sm">{projectName || ''}</span>
                </a>
              </div>
            )}
          </div>
        </div>

        <div className="p-3 border-t border-[#151b26]">
          <div className="bg-[#2c3240] rounded-lg p-4 space-y-4">
            <div className="flex items-center space-x-3">
              <div className="relative w-[26px] h-[26px]">
                <svg className="w-full h-full" viewBox="0 0 26 26">
                  <circle cx="13" cy="13" r="11" fill="none" stroke="#3a3f4a" strokeWidth="4"></circle>
                  <circle
                    cx="13"
                    cy="13"
                    r="11"
                    fill="none"
                    stroke="#4caf50"
                    strokeWidth="4"
                    strokeDasharray="69.115"
                    strokeDashoffset="9.873"
                    transform="rotate(-90 13 13)"
                  ></circle>
                </svg>
              </div>
              <div>
                <p className="text-sm text-white font-medium">Advanced free trial</p>
                <p className="text-sm text-[#4caf50]">12 days left</p>
              </div>
            </div>
            <button className="w-full bg-[#e8990d] text-black font-semibold py-2.5 text-sm rounded-lg hover:bg-yellow-500">
              Add billing info
            </button>
          </div>
          <div className="mt-4 text-center text-xs">
            <span className="text-[#c6c0fc]">Navigation redesign</span>
            <a href="#" className="underline text-[#c6c0fc] ml-2">Send feedback</a>
          </div>
        </div>
      </div>
    </div>
  );
}

const ModeButton = ({ icon, label, active = false }) => {
  const labelColor = active ? 'text-gray-200' : 'text-gray-400';
  const iconContainerBg = active ? 'bg-[#3a3f4a]' : 'bg-transparent';
  const iconColor = active ? 'text-white' : 'text-gray-400';

  return (
    <button className="flex flex-col items-center space-y-1 w-full py-2 rounded-md hover:bg-[#2c3240]">
      <div className={`w-12 h-12 flex items-center justify-center rounded-lg ${iconContainerBg}`}>
        <div className={iconColor}>{icon}</div>
      </div>
      <span className={`text-xs ${labelColor}`}>{label}</span>
    </button>
  );
};

const NavLink = ({ icon, label, active = false }) => {
  const baseClasses = "flex items-center space-x-3 px-2 py-1.5 rounded-md text-sm";
  const activeClasses = active ? "bg-[#3a3f4a] text-gray-100 font-medium" : "text-gray-400 hover:bg-[#3a3f4a] hover:text-gray-100";
  
  return (
    <a href="#" className={`${baseClasses} ${activeClasses}`}>
      {icon}
      <span>{label}</span>
    </a>
  );
};