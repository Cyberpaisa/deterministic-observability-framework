"use client";

import React, { useState, useEffect, useRef } from 'react';
import { Shield, Zap, Lock, Cpu, Globe, MessageSquare, Terminal, Wallet, Send, Users, ListFilter, ExternalLink, Activity, ArrowUpRight } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface Message { role: 'user' | 'assistant' | 'system'; content: string; }
interface Agent { name: string; status: 'ACTIVE' | 'IDLE' | 'BUSY'; role: string; last_log: string; }
interface Issue { agent: string; id: string; title: string; priority?: 'HIGH' | 'NORMAL'; karma_reward?: number; estimated_time?: string; }
interface GraphNode { id: string; label: string; level: number; size: number; }
interface GraphEdge { source: string; target: string; label?: string; }
interface GraphData { nodes: GraphNode[]; edges: GraphEdge[]; }

const StatusRing = ({ value, label, color = "stroke-purple-500" }: { value: number, label: string, color?: string }) => {
  const radius = 30;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (value / 100) * circumference;
  
  return (
    <div className="flex flex-col items-center justify-center relative group">
      <svg className="w-16 h-16 transform -rotate-90">
        <circle cx="32" cy="32" r={radius} stroke="currentColor" strokeWidth="2" fill="transparent" className="text-white/5" />
        <motion.circle 
          cx="32" cy="32" r={radius} stroke="currentColor" strokeWidth="3" fill="transparent"
          strokeDasharray={circumference}
          initial={{ strokeDashoffset: circumference }}
          animate={{ strokeDashoffset: offset }}
          className={color}
          transition={{ duration: 1, ease: "easeOut" }}
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center">
        <span className="text-[10px] font-mono font-black text-white">{value}%</span>
      </div>
      <span className="text-[7px] font-mono text-zinc-500 uppercase mt-2 tracking-widest">{label}</span>
    </div>
  );
};

export default function Dashboard() {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'system', content: 'Connection established via Enigma Sovereign Core.' },
    { role: 'assistant', content: 'Greetings Juan. Identity Enigma #1686 synchronized. Sovereign Office is Online.' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('chat'); // 'chat' | 'swarm' | 'issues' | 'neural'
  const [swarm, setSwarm] = useState<Agent[]>([]);
  const [issues, setIssues] = useState<Issue[]>([]);
  const [graph, setGraph] = useState<GraphData>({ nodes: [], edges: [] });
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, activeTab]);

  const fetchData = async () => {
    try {
      const [sRes, iRes, gRes] = await Promise.all([
        fetch('http://localhost:8005/api/swarm'),
        fetch('http://localhost:8005/api/issues'),
        fetch('http://localhost:8005/api/graph')
      ]);
      if (sRes.ok) setSwarm((await sRes.json()).swarm);
      if (iRes.ok) setIssues((await iRes.json()).issues);
      if (gRes.ok) setGraph(await gRes.json());
    } catch (e) {}
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 10000);
    return () => clearInterval(interval);
  }, []);

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;
    const userMsg = input.trim();
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8005/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMsg, user: 'Juan' })
      });
      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (error) {
      setMessages(prev => [...prev, { role: 'system', content: '⚠️ Neural bridge timeout.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  const [stats, setStats] = useState<any>({ memory_percent: 84, cpu_percent: 42, total_karma: 0, x402_facilitator: 'OFFLINE' });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await fetch('http://localhost:8005/api/stats');
        if (res.ok) setStats(await res.json());
      } catch (e) {}
    };
    fetchStats();
    const interval = setInterval(fetchStats, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-[#020202] text-zinc-300 font-sans selection:bg-purple-500/30 overflow-hidden flex flex-col">
      {/* Visual Foundation - Refined HUD Layer */}
      <div className="fixed inset-0 pointer-events-none">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(88,28,135,0.05)_0%,transparent_70%)]" />
        <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" className="opacity-10">
          <defs>
            <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
              <path d="M 60 0 L 0 0 0 60" fill="none" stroke="white" strokeWidth="0.5" />
              <circle cx="0" cy="0" r="1" fill="white" />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#grid)" />
        </svg>
      </div>
      
      {/* Scanline Overlay - More Subtle */}
      <div className="fixed inset-0 pointer-events-none bg-[linear-gradient(rgba(18,16,16,0)_50%,rgba(0,0,0,0.05)_50%)] z-50 bg-[length:100%_4px] opacity-20" />

      {/* Top Mission Control Bar - Premium Density */}
      <header className="h-16 border-b border-white/10 bg-black/90 backdrop-blur-2xl flex items-center px-8 justify-between shrink-0 z-40 relative">
        <div className="flex items-center gap-6">
           <motion.div 
             whileHover={{ scale: 1.05 }}
             className="w-10 h-10 bg-gradient-to-br from-purple-600 to-indigo-700 rounded-lg flex items-center justify-center shadow-[0_0_20px_rgba(168,85,247,0.4)] border border-white/20"
           >
             <Shield size={20} className="text-white" />
           </motion.div>
           <div className="flex flex-col">
             <span className="text-lg font-black tracking-[-0.05em] text-white leading-none">ENIGMA <span className="text-purple-500">#1686</span></span>
             <span className="text-[9px] font-mono text-zinc-500 uppercase tracking-widest mt-1">SOVEREIGN MISSION CONTROL // LOCAL BRAIN: {stats.status}</span>
           </div>
        </div>

        {/* Scrolling Status Ticker - Refined */}
        <div className="flex-1 mx-16 overflow-hidden border-x border-white/5 h-full flex items-center group cursor-default bg-white/[0.02]">
           <div className="flex gap-16 whitespace-nowrap animate-marquee group-hover:pause italic">
              {[1, 2].map(i => (
                <div key={i} className="flex gap-16 text-[10px] font-mono font-bold text-zinc-500 tracking-wider items-center">
                   <span className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse shadow-[0_0_8px_#10b981]" /> SYS_STABLE</span>
                   <span className="text-white/20">/</span>
                   <span className="flex items-center gap-2 uppercase">UPTIME: {stats.uptime || '14D 02H'}</span>
                   <span className="text-white/20">/</span>
                   <span className="flex items-center gap-2 text-purple-400">KARMA_POOL: +{stats.total_karma} CR</span>
                   <span className="text-white/20">/</span>
                   <span className="flex items-center gap-2 text-indigo-400">SYNC_LATENCY: 12ms</span>
                   <span className="text-white/20">|</span>
                </div>
              ))}
           </div>
        </div>

        <div className="flex items-center gap-8">
           <div className="flex flex-col items-end gap-1">
              <span className="text-[8px] font-mono text-zinc-600 uppercase">Neural Sync</span>
              <div className="w-24 h-1 bg-white/5 rounded-full overflow-hidden border border-white/5">
                <motion.div 
                  initial={{ width: 0 }}
                  animate={{ width: `${stats.neural_sync || 94}%` }}
                  className="h-full bg-purple-500 shadow-[0_0_10px_#a855f7]"
                />
              </div>
           </div>
           <div className="h-8 w-px bg-white/10" />
           <div className="text-[10px] font-mono text-white bg-white/5 px-3 py-1.5 rounded border border-white/10 shadow-inner">
             0x3FA...98DE
           </div>
        </div>
      </header>


      {/* Primary HUD Layout */}
      <main className="flex-1 overflow-hidden grid grid-cols-12 relative">
        
         {/* Navigation Sidebar (Thin) */}
         <aside className="col-span-1 border-r border-white/5 bg-zinc-950/20 flex flex-col items-center py-8 gap-10">
            {[
              { id: 'chat', icon: MessageSquare, label: 'COMMS' },
              { id: 'swarm', icon: Users, label: 'SWARM' },
              { id: 'issues', icon: ListFilter, label: 'TRACKS' },
              { id: 'neural', icon: Activity, label: 'NEURAL' },
              { id: 'lab', icon: Zap, label: 'LAB' }
            ].map((it) => (
              <button 
               key={it.id} 
               onClick={() => setActiveTab(it.id as any)}
               className={`group flex flex-col items-center gap-2 transition-all ${activeTab === it.id ? 'opacity-100' : 'opacity-40 hover:opacity-100'}`}
              >
                 <div className={`p-4 rounded-2xl border transition-all ${activeTab === it.id ? 'bg-purple-600/20 border-purple-500 shadow-[0_0_20px_rgba(168,85,247,0.3)]' : 'bg-transparent border-transparent group-hover:bg-white/5'}`}>
                    <it.icon size={22} className={activeTab === it.id ? 'text-white' : 'text-zinc-500 group-hover:text-zinc-300'} />
                 </div>
                 <span className="text-[7px] font-mono font-black tracking-[0.3em] uppercase">{it.label}</span>
              </button>
            ))}
            <div className="mt-auto flex flex-col items-center gap-6 pb-4">
               <div className="w-10 h-10 rounded-full border border-white/10 bg-gradient-to-br from-indigo-500 to-purple-500 p-[1px] hover:scale-110 transition-all cursor-pointer">
                  <div className="w-full h-full rounded-full bg-black flex items-center justify-center">
                     <Users size={16} className="text-white" />
                  </div>
               </div>
            </div>
         </aside>


        {/* Global HUD Content Area */}
        <section className="col-span-8 flex flex-col bg-black/40 relative">
           <AnimatePresence mode="wait">
             {activeTab === 'chat' && (
               <motion.div key="chat" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="h-full flex flex-col p-8 lg:p-12 relative overflow-hidden">
                  <div className="absolute top-0 right-0 p-8 opacity-[0.02] pointer-events-none">
                     <MessageSquare size={300} />
                  </div>
                  
                  <div ref={scrollRef} className="flex-1 space-y-10 overflow-y-auto pr-4 custom-scrollbar relative z-10">
                     {messages.map((m, i) => (
                       <motion.div 
                         key={i} 
                         initial={{ opacity: 0, x: m.role === 'user' ? 20 : -20 }}
                         animate={{ opacity: 1, x: 0 }}
                         className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}
                       >
                          <div className={`max-w-[80%] p-6 rounded-2xl border transition-all ${
                            m.role === 'user' 
                            ? 'bg-purple-600/10 border-purple-500/40 text-white shadow-[0_0_30px_rgba(168,85,247,0.1)]' 
                            : m.role === 'system'
                            ? 'bg-transparent border-zinc-800/50 text-zinc-500 font-mono text-[9px] uppercase tracking-[0.2em] py-2 px-4 italic'
                            : 'bg-zinc-900/80 border-white/10 text-zinc-300 backdrop-blur-xl shadow-2xl'
                          }`}>
                             {m.role === 'assistant' && (
                               <div className="flex items-center gap-3 mb-3 pb-3 border-b border-white/5">
                                  <div className="w-2 h-2 bg-purple-500 rounded-full animate-pulse" />
                                  <span className="text-[10px] font-mono font-black text-purple-400 uppercase tracking-widest">Enigma_v27.4 // Response</span>
                               </div>
                             )}
                             <p className={`leading-relaxed ${m.role === 'assistant' ? 'text-sm' : 'text-xs opacity-90'}`}>
                                {m.content}
                             </p>
                             {m.role === 'assistant' && (
                               <div className="mt-4 pt-4 border-t border-white/5 flex justify-between items-center text-[8px] font-mono text-zinc-600">
                                  <span>SYNC_ENCRYPTION: AES-256</span>
                                  <span>TTL: 3600S</span>
                               </div>
                             )}
                          </div>
                       </motion.div>
                     ))}
                     {isLoading && (
                       <div className="flex flex-col gap-2">
                          <div className="flex items-center gap-2 text-[10px] font-mono text-purple-500 font-bold uppercase tracking-widest animate-pulse">
                             <Zap size={10} className="animate-bounce" /> Processing_Neural_Stream...
                          </div>
                          <div className="w-48 h-1 bg-white/5 rounded-full overflow-hidden">
                             <motion.div 
                               animate={{ x: [-200, 200] }}
                               transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
                               className="w-20 h-full bg-gradient-to-r from-transparent via-purple-500 to-transparent"
                             />
                          </div>
                       </div>
                     )}
                  </div>

                  <div className="mt-8 flex gap-4 relative z-10 pt-6 border-t border-white/5">
                     <div className="flex-1 relative group">
                        <div className="absolute -inset-1 bg-gradient-to-r from-purple-600/20 to-indigo-600/20 blur-xl group-focus-within:opacity-100 opacity-0 transition-opacity rounded-full" />
                        <div className="absolute left-6 top-1/2 -translate-y-1/2 text-zinc-600">
                           <Terminal size={16} />
                        </div>
                        <input 
                          type="text" value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                          placeholder="ENTER_SOVEREIGN_COMMAND..."
                          className="w-full bg-black/60 border border-white/10 rounded-full py-5 px-14 text-sm focus:outline-none focus:border-purple-500/50 transition-all text-white font-mono placeholder:text-zinc-700 backdrop-blur-md"
                        />
                        <button 
                          onClick={handleSend}
                          className="absolute right-4 top-1/2 -translate-y-1/2 p-2 bg-purple-600 hover:bg-purple-500 text-white rounded-full transition-all shadow-[0_0_15px_rgba(168,85,247,0.4)] hover:scale-110 active:scale-95"
                        >
                           <Send size={16} />
                        </button>
                     </div>
                  </div>
               </motion.div>
             )}


             {activeTab === 'swarm' && (
               <motion.div key="swarm" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="h-full p-8 grid grid-cols-2 lg:grid-cols-3 gap-6 overflow-y-auto custom-scrollbar">
                  {swarm.map((agent, idx) => (
                    <motion.div 
                      key={agent.name} 
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: idx * 0.1 }}
                      className="bg-zinc-950/80 border border-white/10 rounded-2xl p-6 relative overflow-hidden group hover:border-purple-500/50 transition-all shadow-[0_0_20px_rgba(0,0,0,0.5)]"
                    >
                       {/* Neural Pulse Animation Background */}
                       <div className="absolute inset-0 opacity-10 pointer-events-none overflow-hidden">
                          <motion.div 
                            animate={{ scale: [1, 1.2, 1], opacity: [0.1, 0.3, 0.1] }}
                            transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                            className="absolute -top-1/2 -left-1/2 w-full h-full bg-purple-500/20 blur-[100px] rounded-full"
                          />
                       </div>

                       <div className="flex justify-between items-start mb-6 relative z-10">
                          <div className="flex flex-col">
                             <div className="flex items-center gap-2">
                                <div className={`w-2 h-2 rounded-full ${agent.status === 'ACTIVE' ? 'bg-emerald-500 animate-pulse shadow-[0_0_8px_#10b981]' : 'bg-zinc-700'}`} />
                                <span className="text-xl font-black text-white tracking-tighter">{agent.name}</span>
                             </div>
                             <span className="text-[9px] font-mono text-zinc-500 uppercase tracking-widest mt-1">{agent.role} CORE_UNIT</span>
                          </div>
                          <div className="p-2 bg-white/5 rounded-lg border border-white/10">
                             <Terminal size={14} className="text-zinc-500 group-hover:text-purple-400 transition-colors" />
                          </div>
                       </div>

                       {/* Mini Terminal Simulator */}
                       <div className="bg-black/50 rounded-lg p-3 mb-6 border border-white/5 font-mono text-[8px] h-20 overflow-hidden relative group-hover:border-purple-500/20 transition-all">
                          <div className="text-emerald-500/60 mb-1 leading-tight">{">"} INITIALIZING_COGNITIVE_STEP...</div>
                          <div className="text-zinc-600 mb-1 leading-tight">{">"} ANALYZING_BUFFER_STREAM_0x{idx}F2</div>
                          <div className="text-zinc-400 mb-1 leading-tight animate-pulse">{">"} MISSION: {agent.role.toUpperCase()}_OPTIMIZATION</div>
                          <div className="text-purple-500/40 mt-2">{">"} STATUS: {agent.status}</div>
                          <motion.div 
                            animate={{ y: [0, -40] }}
                            transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
                            className="absolute bottom-0 left-3 right-3 h-1 bg-white/[0.02]"
                          />
                       </div>

                       <div className="grid grid-cols-2 gap-3 relative z-10">
                          {[
                            { label: 'Latency', val: (agent as any).latency || '24ms', icon: Activity },
                            { label: 'Energy', val: (agent as any).throughput || '1.4 tps', icon: Zap }
                          ].map(it => (
                            <div key={it.label} className="bg-white/5 p-3 rounded-xl border border-white/5 flex flex-col gap-1">
                               <div className="flex justify-between items-center">
                                  <span className="text-[7px] font-mono text-zinc-600 uppercase">{it.label}</span>
                                  <it.icon size={10} className="text-zinc-700" />
                               </div>
                               <div className="text-xs font-mono font-black text-white">{it.val}</div>
                            </div>
                          ))}
                       </div>

                       {/* Progress Bar (Working Indicator) */}
                       <div className="mt-6">
                          <div className="flex justify-between text-[7px] font-mono text-zinc-600 mb-2">
                             <span>TASK_PROGRESS</span>
                             <span>{agent.status === 'ACTIVE' ? '82%' : '0%'}</span>
                          </div>
                          <div className="w-full h-1 bg-white/5 rounded-full overflow-hidden">
                             <motion.div 
                               initial={{ width: 0 }}
                               animate={{ width: agent.status === 'ACTIVE' ? '82%' : '5%' }}
                               className={`h-full ${agent.status === 'ACTIVE' ? 'bg-purple-500 shadow-[0_0_10px_#a855f7]' : 'bg-zinc-800'}`}
                             />
                          </div>
                       </div>
                    </motion.div>
                  ))}
               </motion.div>
             )}


             {activeTab === 'issues' && (
               <motion.div key="issues" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="h-full p-8 flex flex-col gap-6 overflow-y-auto custom-scrollbar">
                  <div className="flex justify-between items-center border-b border-white/10 pb-4">
                     <div>
                        <span className="text-xs font-black text-white tracking-[0.4em] uppercase">Tactical Backlog Registry</span>
                        <div className="text-[8px] font-mono text-zinc-600 mt-1 uppercase">SYNC_STATUS: VERIFIED // HACKATHON_TRACKS: 03/03</div>
                     </div>
                     <span className="bg-white/5 px-4 py-2 rounded-xl border border-white/10 text-[10px] font-mono text-purple-400 font-bold">
                        {issues.length} MISSIONS_REMAINING
                     </span>
                  </div>
                  
                  <div className="grid grid-cols-1 gap-2">
                    {issues.map((issue, idx) => (
                      <motion.div 
                        key={issue.id} 
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: idx * 0.05 }}
                        className="bg-white/[0.02] border border-white/5 p-5 rounded-2xl flex items-center justify-between group hover:bg-white/5 hover:border-purple-500/30 transition-all cursor-pointer relative overflow-hidden"
                      >
                         <div className="absolute inset-y-0 left-0 w-1 bg-purple-500 opacity-20 group-hover:opacity-100 transition-opacity" />
                         <div className="flex items-center gap-8 relative z-10 w-full">
                            <div className="text-[10px] font-mono text-zinc-700 w-12">{idx + 1}.</div>
                            <div className={`w-2 h-2 rounded-full ${issue.priority === 'HIGH' ? 'bg-amber-500 shadow-[0_0_8px_#f59e0b]' : 'bg-purple-500 shadow-[0_0_8px_#a855f7]'}`} />
                            
                            <div className="grid grid-cols-4 items-center gap-12 flex-1">
                               <div className="col-span-2">
                                  <div className="text-[8px] font-mono text-zinc-500 mb-1 flex items-center gap-2">
                                     <span className="bg-white/10 px-1.5 py-0.5 rounded text-white italic">@{issue.agent.toUpperCase()}</span> 
                                     ID: {issue.id.split('-')[0]}
                                  </div>
                                  <div className="text-sm font-bold text-white tracking-tight group-hover:text-purple-300 transition-colors uppercase">
                                     {issue.title.replace('.md','').replace(/_/g, ' ')}
                                  </div>
                               </div>
                               
                               <div className="text-right">
                                  <div className="text-[8px] font-mono text-zinc-600 uppercase mb-1">Time Alloc</div>
                                  <div className="text-[10px] font-mono font-black text-zinc-400">{issue.estimated_time || '30m'}</div>
                               </div>
                               
                               <div className="text-right">
                                  <div className="text-[8px] font-mono text-zinc-600 uppercase mb-1">Karma Reward</div>
                                  <div className="text-[10px] font-mono font-black text-emerald-400">+{issue.karma_reward} CR</div>
                               </div>
                            </div>
                         </div>
                         <ArrowUpRight size={14} className="text-zinc-800 group-hover:text-white transition-all transform group-hover:-translate-y-1 group-hover:translate-x-1" />
                      </motion.div>
                    ))}
                  </div>

                  {/* Empty State / Bottom Deco */}
                  <div className="mt-auto pt-8 border-t border-white/5 flex justify-center">
                     <span className="text-[8px] font-mono text-zinc-800 tracking-[1em] uppercase">End of Registry Trace</span>
                  </div>
               </motion.div>
             )}


             {activeTab === 'neural' && (
               <motion.div key="neural" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="h-full relative overflow-hidden flex items-center justify-center bg-zinc-950/20">
                  {/* Background Neural Grid */}
                  <div className="absolute inset-0 opacity-20 group">
                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(168,85,247,0.1)_0%,transparent_50%)]" />
                  </div>

                  <svg className="w-full h-full absolute inset-0 z-0">
                     {graph.edges.map((edge, i) => {
                        const source = graph.nodes.find(n => n.id === edge.source);
                        const target = graph.nodes.find(n => n.id === edge.target);
                        if (!source || !target) return null;
                        
                        // Calculate positions based on levels
                        const x1 = `${(source.level - 1) * 30 + 10}%`;
                        const y1 = `${20 + (graph.nodes.filter(n => n.level === source.level).indexOf(source) * 20)}%`;
                        const x2 = `${(target.level - 1) * 30 + 10}%`;
                        const y2 = `${20 + (graph.nodes.filter(n => n.level === target.level).indexOf(target) * 20)}%`;
                        
                        return (
                          <g key={i}>
                            <motion.path 
                              d={`M ${x1} ${y1} L ${x2} ${y2}`}
                              stroke="url(#edgeGradient)"
                              strokeWidth="1"
                              strokeOpacity="0.3"
                              fill="none"
                              initial={{ pathLength: 0 }}
                              animate={{ pathLength: 1 }}
                              transition={{ duration: 2, delay: i * 0.1 }}
                            />
                            {/* Animated Pulse along the path */}
                            <circle r="2" fill="#a855f7" className="shadow-[0_0_8px_#a855f7]">
                               <animateMotion 
                                 dur={`${2 + Math.random() * 2}s`} 
                                 repeatCount="indefinite" 
                                 path={`M ${x1} ${y1} L ${x2} ${y2}`} 
                               />
                            </circle>
                          </g>
                        );
                     })}
                     <defs>
                        <linearGradient id="edgeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                           <stop offset="0%" stopColor="#6366f1" />
                           <stop offset="100%" stopColor="#a855f7" />
                        </linearGradient>
                     </defs>
                  </svg>
                  
                  <div className="flex justify-between w-full px-20 relative z-10">
                     {[1, 2, 3, 4].map(level => (
                       <div key={level} className="flex flex-col gap-8 items-center">
                          <span className="text-[7px] font-mono text-zinc-700 tracking-[0.6em] uppercase mb-4 py-1 px-3 border border-white/5 rounded-full bg-white/[0.02]">Tier {level}</span>
                          {graph.nodes.filter(n => n.level === level).map(node => (
                            <motion.div 
                              key={node.id} 
                              whileHover={{ scale: 1.1, borderColor: "rgba(168,85,247,0.5)" }}
                              className="bg-black/80 border border-white/10 p-4 rounded-2xl w-40 text-center relative group backdrop-blur-xl shadow-2xl"
                            >
                               <div className="absolute -inset-1 bg-gradient-to-r from-indigo-500/20 to-purple-500/20 blur opacity-0 group-hover:opacity-100 transition-opacity rounded-2xl" />
                               <div className="text-[10px] font-black text-white tracking-tight uppercase relative z-10">{node.label}</div>
                               <div className="flex justify-center gap-1 mt-2 relative z-10">
                                  {[1,2,3].map(dot => (
                                    <div key={dot} className="w-1 h-1 bg-purple-500/40 rounded-full" />
                                  ))}
                               </div>
                               <div className="text-[6px] font-mono text-zinc-500 mt-2 uppercase tracking-widest relative z-10">Neural_ID: {node.id.slice(0, 6)}</div>
                            </motion.div>
                          ))}
                       </div>
                     ))}
                  </div>
                  
                  {/* Legend / Info Overlay */}
                  <div className="absolute bottom-10 right-10 flex flex-col items-end gap-2 p-4 bg-black/40 border border-white/5 rounded-2xl backdrop-blur-md">
                     <span className="text-[8px] font-mono text-zinc-500 uppercase">Connectivity Map v27.4</span>
                     <div className="flex items-center gap-2">
                        <div className="w-2 h-2 rounded-full bg-emerald-500 shadow-[0_0_5px_#10b981]" />
                        <span className="text-[9px] font-mono text-white">AUTONOMOUS_ORCHESTRATION</span>
                     </div>
                  </div>
               </motion.div>
             )}

           </AnimatePresence>
        </section>

        {/* Right HUD Panels */}
        <aside className="col-span-3 border-l border-white/5 bg-zinc-950/40 p-6 flex flex-col gap-6 overflow-y-auto">
           
            {/* Telemetry HUD Cards - Replaced with Status Rings */}
            <div className="space-y-6">
               <div className="text-[10px] font-black text-zinc-500 tracking-[0.5em] mb-6 uppercase border-b border-white/5 pb-2">Vital Telemetry</div>
               <div className="grid grid-cols-1 gap-8 py-4">
                  <div className="flex justify-around items-center bg-white/[0.02] border border-white/5 py-8 rounded-3xl backdrop-blur-sm">
                    <StatusRing value={stats.cpu_percent || 0} label="Core Load" color="stroke-indigo-500" />
                    <StatusRing value={stats.memory_percent || 0} label="Sync RAM" color="stroke-purple-500" />
                    <StatusRing value={stats.neural_sync || 94.2} label="Neural" color="stroke-emerald-500" />
                  </div>
               </div>
               
               <div className="bg-zinc-950/80 border border-white/10 p-5 rounded-2xl flex flex-col gap-4">
                  <div className="flex justify-between items-center text-[8px] font-mono text-zinc-500 uppercase tracking-widest">
                    <span>Inference Engine</span>
                    <span className="text-emerald-500">OPTIMIZED</span>
                  </div>
                  <div className="flex items-end justify-between">
                    <span className="text-xl font-black text-white italic">OLLAMA: Llama3-8B</span>
                    <span className="text-[10px] font-mono text-indigo-400">12.4 GB ACTIVE</span>
                  </div>
               </div>
            </div>

            {/* Ultravioleta DAO Ecosystem Panel - Premium Glassmorphism */}
            <div className="bg-gradient-to-br from-zinc-900/80 to-black border border-white/10 rounded-3xl p-6 relative overflow-hidden shadow-2xl">
               <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-purple-500/60 to-transparent" />
               <div className="flex items-center gap-3 mb-8">
                  <div className="w-2 h-2 bg-purple-500 rounded-full animate-ping" />
                  <span className="text-[10px] font-black text-white tracking-[0.3em] uppercase">Sovereign Registry</span>
               </div>
               <div className="space-y-3">
                 {[
                   { name: 'Karma Connector', val: 'ACTIVE', color: 'text-emerald-400' },
                   { name: 'x402 Settlement', val: 'PENDING', color: 'text-amber-400' },
                   { name: 'Cognee Layer', val: 'SYNCED', color: 'text-indigo-400' }
                 ].map(tool => (
                   <div key={tool.name} className="flex items-center justify-between p-3 bg-white/5 border border-white/5 rounded-xl group hover:bg-white/[0.08] transition-all cursor-pointer">
                      <span className="text-[9px] font-mono font-black text-zinc-500 group-hover:text-zinc-300 transition-colors uppercase">{tool.name}</span>
                      <span className={`text-[8px] font-mono font-bold ${tool.color}`}>{tool.val}</span>
                   </div>
                 ))}
               </div>

               <div className="mt-10 pt-8 border-t border-white/10">
                  <div className="flex justify-between items-end">
                     <div className="flex flex-col gap-1">
                        <span className="text-[9px] font-mono text-zinc-600 uppercase tracking-widest">Treasury Balance</span>
                        <span className="text-4xl font-black text-white tracking-tighter shadow-sm">{stats.total_karma || 0}<span className="text-sm font-mono text-purple-500 ml-1">ᛝ</span></span>
                     </div>
                  </div>
               </div>
            </div>

            {/* Manual / Links */}
            <button className="w-full py-5 border border-zinc-800 bg-white/[0.02] rounded-2xl text-[10px] font-black text-zinc-500 uppercase tracking-[0.4em] hover:border-purple-500/50 hover:text-white transition-all shadow-inner group">
               <span className="group-hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">EXEC_HANDSHAKE_NODE_01</span>
            </button>
         </aside>

      </main>

      <style jsx global>{`
        @keyframes marquee {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
        }
        .animate-marquee {
          animation: marquee 30s linear infinite;
        }
        .pause { animation-play-state: paused; }
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #3f3f46; border-radius: 10px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #52525b; }
      `}</style>
    </div>
  );
}
