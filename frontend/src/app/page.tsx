"use client";

import React, { useState, useEffect, useRef } from 'react';
import { Shield, Zap, Lock, Cpu, Globe, MessageSquare, Terminal, Wallet, Send, Users, ListFilter, ExternalLink, Activity, ArrowUpRight } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface Message { role: 'user' | 'assistant' | 'system'; content: string; }
interface Agent { name: string; status: 'ACTIVE' | 'IDLE' | 'BUSY'; role: string; last_log: string; }
interface Issue { agent: string; id: string; title: string; priority?: 'HIGH' | 'NORMAL'; karma_reward?: number; }
interface GraphNode { id: string; label: string; level: number; size: number; }
interface GraphEdge { source: string; target: string; label?: string; }
interface GraphData { nodes: GraphNode[]; edges: GraphEdge[]; }

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
    <div className="min-h-screen bg-[#020202] text-white font-sans selection:bg-purple-500/30">
      {/* Background Decor */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-[10%] -left-[10%] w-[50%] h-[50%] bg-purple-900/10 blur-[150px] rounded-full" />
        <div className="absolute top-[20%] -right-[10%] w-[40%] h-[40%] bg-blue-900/10 blur-[150px] rounded-full" />
      </div>

      <nav className="sticky top-0 z-50 border-b border-white/5 bg-black/60 backdrop-blur-2xl">
        <div className="max-w-7xl mx-auto px-6 h-18 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 bg-gradient-to-br from-purple-600 to-indigo-700 rounded-xl flex items-center justify-center shadow-lg shadow-purple-500/20">
              <Shield size={20} className="text-white" />
            </div>
            <div className="flex flex-col">
               <span className="font-black tracking-tighter text-2xl leading-none">DOF <span className="text-purple-500 italic">OS</span></span>
               <span className="text-[10px] text-zinc-500 font-mono tracking-widest uppercase">Ultravioleta Edition</span>
            </div>
          </div>
          <div className="hidden md:flex items-center gap-10 text-xs font-bold text-zinc-400 tracking-widest uppercase">
            <span className="text-emerald-500 flex items-center gap-1"><span className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse" /> SOVEREIGN NODE ACTIVE</span>
            <a href="https://ultravioletadao.xyz/" target="_blank" className="hover:text-white transition-colors cursor-pointer">DAO TOOLS</a>
            <span className="cursor-pointer hover:text-white transition-colors">OFFICE</span>
          </div>
          <div className="flex items-center gap-4">
             <div className="text-[10px] font-mono text-zinc-500 text-right hidden sm:block">
                M4 MAX // 36GB RAM<br/>
                LATENCY: 12ms
             </div>
             <button className="px-5 py-2.5 bg-white text-black text-xs font-black rounded-full hover:bg-zinc-200 transition-all active:scale-95 shadow-xl">
               ENIGMA #1686
             </button>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-6 py-8 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 h-[calc(100vh-160px)]">
          
          {/* Main Workspace (Left) */}
          <div className="lg:col-span-9 flex flex-col bg-zinc-900/40 border border-white/5 rounded-[40px] overflow-hidden backdrop-blur-xl shadow-2xl relative">
             
             {/* Integrated Tabs System */}
             <div className="px-8 pt-6 pb-2 border-b border-white/5 bg-white/5 flex items-center gap-8">
                {['chat', 'swarm', 'issues', 'neural'].map(tab => (
                  <button 
                    key={tab} 
                    onClick={() => setActiveTab(tab)}
                    className={`pb-4 text-xs font-black tracking-[0.2em] uppercase transition-all relative ${activeTab === tab ? 'text-purple-500' : 'text-zinc-500 hover:text-zinc-300'}`}
                  >
                    {tab}
                    {activeTab === tab && <motion.div layoutId="tab-underline" className="absolute bottom-0 left-0 right-0 h-0.5 bg-purple-500 shadow-[0_0_10px_#a855f7]" />}
                  </button>
                ))}
             </div>

             <div className="flex-1 overflow-hidden relative">
               <AnimatePresence mode="wait">
                 {activeTab === 'chat' && (
                   <motion.div 
                    key="chat"
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    className="h-full flex flex-col p-8"
                   >
                     <div ref={scrollRef} className="flex-1 space-y-6 overflow-y-auto pr-4 scroll-smooth">
                        {messages.map((m, i) => (
                          <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                            <div className={`max-w-[75%] p-5 rounded-[24px] text-sm leading-relaxed ${
                              m.role === 'user' 
                              ? 'bg-purple-600 text-white shadow-lg shadow-purple-500/20' 
                              : m.role === 'system'
                              ? 'bg-zinc-800/30 text-zinc-500 font-mono text-[9px] border border-white/5' 
                              : 'bg-zinc-800/80 border border-white/10 text-zinc-200 backdrop-blur-md'
                            }`}>
                              {m.role === 'assistant' && <div className="text-[9px] font-black text-purple-400 mb-2 tracking-[0.3em] uppercase opacity-60">ENIGMA // MASTER</div>}
                              {m.content}
                            </div>
                          </div>
                        ))}
                        {isLoading && (
                          <div className="flex justify-start"><div className="w-12 h-6 bg-white/5 rounded-full animate-pulse" /></div>
                        )}
                     </div>

                     <div className="mt-6 relative">
                        <input 
                          type="text" 
                          value={input}
                          onChange={(e) => setInput(e.target.value)}
                          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                          placeholder="Execute mission order..." 
                          className="w-full bg-black/60 border border-white/10 rounded-3xl px-8 py-5 text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/50 transition-all backdrop-blur-xl placeholder:text-zinc-600"
                        />
                        <button 
                          onClick={handleSend}
                          disabled={isLoading}
                          className="absolute right-4 top-1/2 -translate-y-1/2 p-3 bg-white text-black rounded-2xl hover:bg-purple-500 hover:text-white transition-all disabled:opacity-50 shadow-xl"
                        >
                          <Send size={20} />
                        </button>
                     </div>
                   </motion.div>
                 )}

                 {activeTab === 'swarm' && (
                   <motion.div 
                    key="swarm"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    className="p-10 grid grid-cols-1 md:grid-cols-2 gap-6"
                   >
                      {swarm.map(agent => (
                        <div key={agent.name} className="p-6 bg-zinc-800/50 border border-white/5 rounded-[32px] flex items-center gap-6 group hover:bg-zinc-800 transition-all">
                           <div className={`w-14 h-14 rounded-2xl flex items-center justify-center ${agent.status === 'ACTIVE' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-zinc-700/50 text-zinc-500'}`}>
                              <Users size={24} />
                           </div>
                           <div className="flex-1">
                              <h4 className="font-bold text-lg">{agent.name}</h4>
                              <p className="text-xs text-zinc-500 tracking-widest">{agent.role.toUpperCase()} SPECIALIST</p>
                           </div>
                           <div className={`px-3 py-1 rounded-full text-[9px] font-black tracking-tighter ${agent.status === 'ACTIVE' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-zinc-700 text-zinc-500'}`}>
                              {agent.status}
                           </div>
                        </div>
                      ))}
                   </motion.div>
                 )}

                 {activeTab === 'issues' && (
                   <motion.div 
                    key="issues"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    className="p-10 space-y-4"
                   >
                      <h3 className="text-xs font-black text-zinc-500 tracking-[0.4em] mb-6 uppercase">Active Backlog</h3>
                       {issues.map(issue => (
                        <div key={issue.id} className={`p-5 bg-white/5 border-l-4 ${issue.priority === 'HIGH' ? 'border-amber-500' : 'border-purple-500'} rounded-r-2xl flex items-center justify-between hover:bg-white/10 transition-all group`}>
                           <div className="flex items-center gap-4">
                              <div className={`text-[10px] ${issue.priority === 'HIGH' ? 'bg-amber-500/10 text-amber-400' : 'bg-purple-500/10 text-purple-400'} px-2 py-1 rounded-md font-mono font-bold tracking-tighter`}>{issue.agent.toUpperCase()}</div>
                              <div className="flex flex-col">
                                <span className="text-sm font-medium">{issue.title.replace('.md', '').replace(/_/g, ' ')}</span>
                                <span className="text-[9px] font-black text-zinc-500 uppercase tracking-[0.2em] mt-1">Reward: {issue.karma_reward} Karma</span>
                              </div>
                           </div>
                           <div className="flex items-center gap-4">
                              {issue.priority === 'HIGH' && <Zap size={14} className="text-amber-500 animate-pulse" />}
                              <ListFilter size={16} className="text-zinc-600 group-hover:text-purple-400 transition-colors" />
                           </div>
                        </div>
                      ))}
                      {issues.length === 0 && <div className="text-center py-20 text-zinc-600 font-mono text-sm tracking-widest leading-loose">NO ACTIVE ISSUES.<br/>WAITING FOR MISSION ASSIGNMENT.</div>}
                   </motion.div>
                 )}
                 {activeTab === 'neural' && (
                   <motion.div 
                    key="neural"
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 1.05 }}
                    className="h-full relative overflow-hidden flex items-center justify-center p-10"
                   >
                       <svg className="w-full h-full absolute inset-0 opacity-40 pointer-events-none">
                          {graph.edges.map((edge, i) => {
                             const source = graph.nodes.find(n => n.id === edge.source);
                             const target = graph.nodes.find(n => n.id === edge.target);
                             if (!source || !target) return null;
                             
                             const x1 = `${source.level * 25}%`;
                             const y1 = `${10 * (i + 1)}%`;
                             const x2 = `${target.level * 25}%`;
                             const y2 = `${20 * (i + 1)}%`;

                             return (
                               <g key={i}>
                                 <line x1={x1} y1={y1} x2={x2} y2={y2} stroke="white" strokeWidth="0.5" strokeDasharray="4 4" className="opacity-30" />
                                 {edge.label && (
                                   <text 
                                     x="50%" 
                                     y="50%" 
                                     className="text-[8px] fill-zinc-500 font-black tracking-widest uppercase"
                                     style={{ transform: `translate(calc(${x1} + (${x2} - ${x1})/2), calc(${y1} + (${y2} - ${y1})/2))` }}
                                   >
                                     {edge.label}
                                   </text>
                                 )}
                               </g>
                             );
                          })}
                       </svg>
                      
                      <div className="grid grid-cols-4 gap-12 w-full relative z-10">
                         {[1, 2, 3, 4].map(level => (
                           <div key={level} className="flex flex-col gap-6 items-center">
                              <div className="text-[10px] font-black text-zinc-600 tracking-[0.4em] uppercase mb-4">Level {level}</div>
                              {graph.nodes.filter(n => n.level === level).map(node => (
                                <motion.div 
                                  key={node.id}
                                  whileHover={{ scale: 1.1, backgroundColor: 'rgba(168, 85, 247, 0.2)' }}
                                  className="w-full p-4 bg-white/5 border border-white/10 rounded-2xl flex flex-col items-center gap-2 text-center group transition-all"
                                >
                                   <div className={`w-3 h-3 rounded-full ${level === 1 ? 'bg-white' : level === 2 ? 'bg-purple-500' : 'bg-zinc-500'} animate-pulse`} />
                                   <span className="text-[10px] font-bold group-hover:text-purple-400">{node.label}</span>
                                </motion.div>
                              ))}
                           </div>
                         ))}
                      </div>
                      
                      <div className="absolute bottom-10 right-10 bg-black/80 border border-purple-500/30 p-4 rounded-2xl backdrop-blur-xl">
                         <div className="text-[9px] font-black text-purple-500 uppercase mb-1">Intelligence Sync</div>
                         <div className="text-xl font-black">94.2%</div>
                      </div>
                   </motion.div>
                 )}
               </AnimatePresence>
             </div>
          </div>

          {/* Right Sidebar */}
          <div className="lg:col-span-3 flex flex-col gap-6">
             {/* Resources */}
             <div className="bg-zinc-900/40 border border-white/5 rounded-[40px] p-8 backdrop-blur-xl shadow-xl">
                <div className="flex items-center gap-3 mb-8">
                   <Activity size={18} className="text-purple-500" />
                   <h4 className="text-[11px] font-black tracking-[0.2em] text-zinc-400">TELEMETRY</h4>
                </div>
                <div className="space-y-8">
                   <div>
                      <div className="flex justify-between text-[10px] text-zinc-500 mb-3 font-mono"><span>RAM/36GB</span><span>{Math.round(stats.memory_percent)}%</span></div>
                      <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
                         <div className="h-full bg-purple-500 shadow-[0_0_15px_#a855f7] transition-all duration-1000" style={{ width: `${stats.memory_percent}%` }} />
                      </div>
                   </div>
                   <div>
                      <div className="flex justify-between text-[10px] text-zinc-500 mb-3 font-mono"><span>CPU/M4MAX</span><span>{Math.round(stats.cpu_percent)}%</span></div>
                      <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
                         <div className="h-full bg-indigo-500 shadow-[0_0_15px_#6366f1] transition-all duration-1000" style={{ width: `${stats.cpu_percent}%` }} />
                      </div>
                   </div>
                </div>
             </div>

             {/* Ultravioleta DAO Tools Panel */}
             <div className="p-8 bg-white/5 border border-white/5 rounded-[40px] backdrop-blur-3xl overflow-hidden shrink-0">
                <div className="flex items-center gap-4 mb-8">
                   <div className="w-12 h-12 bg-purple-500/10 border border-purple-500/20 rounded-2xl flex items-center justify-center text-purple-500">
                      <Zap size={24} />
                   </div>
                   <div>
                      <h3 className="text-sm font-black tracking-widest uppercase">UltraVioleta DAO</h3>
                      <p className="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Active Tools & Economy</p>
                   </div>
                </div>

                <div className="space-y-4">
                   {[
                      { name: 'Karma-Hello', desc: 'Reputation & UVD Economy', link: 'https://karma-hello.xyz/' },
                      { name: 'Cognee Graph', desc: 'Neural Knowledge Layer', link: 'https://cognee.ai/' },
                      { name: 'Sovereign Repo', desc: 'Private Vault Control', link: 'https://github.com/Cyberpaisa/deterministic-observability-framework' },
                      { name: 'Ollama Intelligence', desc: 'Local LLM Node (M4 Max)', link: 'http://localhost:11434' }
                   ].map(tool => (
                      <a 
                        key={tool.name} 
                        href={tool.link}
                        target="_blank"
                        className="block p-5 bg-white/5 border border-white/5 rounded-3xl group hover:border-purple-500/30 transition-all"
                      >
                         <div className="flex items-center justify-between mb-2">
                            <span className="text-xs font-black tracking-widest uppercase group-hover:text-purple-400 transition-colors">{tool.name}</span>
                            <ArrowUpRight size={14} className="text-zinc-600 group-hover:text-purple-500 transition-all transform group-hover:-translate-y-0.5 group-hover:translate-x-0.5" />
                         </div>
                         <p className="text-[10px] text-zinc-600 font-bold uppercase tracking-wider">{tool.desc}</p>
                      </a>
                   ))}
                </div>
                 <div className="mt-8 pt-8 border-t border-white/5 space-y-6">
                    <div>
                       <div className="flex items-center justify-between mb-2">
                          <span className="text-[10px] font-black text-zinc-500 uppercase tracking-widest">x402 Facilitator</span>
                          <span className={`text-[9px] font-black uppercase tracking-widest px-2 py-0.5 rounded-md ${stats.x402_facilitator === 'ONLINE' ? 'bg-emerald-500/10 text-emerald-500' : 'bg-zinc-800 text-zinc-600'}`}>
                             {stats.x402_facilitator}
                          </span>
                       </div>
                       <div className="text-[10px] font-mono text-zinc-600">ID: UVD-FAC-8120-X</div>
                    </div>

                    <div>
                       <div className="flex items-center justify-between mb-4">
                          <span className="text-[10px] font-black text-zinc-500 uppercase tracking-widest">Vault Status</span>
                          <span className="text-[10px] font-black text-green-500 uppercase tracking-widest flex items-center gap-2">
                             <div className="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse" />
                             Encrypted
                          </span>
                       </div>
                       <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                          <motion.div 
                            initial={{ width: 0 }}
                            animate={{ width: '88%' }}
                            className="h-full bg-gradient-to-r from-purple-500 to-indigo-500 shadow-[0_0_10px_#a855f7]"
                          />
                       </div>
                    </div>

                    <div className="p-4 bg-purple-500/5 border border-purple-500/10 rounded-2xl">
                       <div className="text-[9px] font-black text-zinc-500 uppercase mb-2">Internal Karma Balance</div>
                       <div className="flex items-baseline gap-2">
                          <span className="text-2xl font-black text-white">{stats.total_karma || 0}</span>
                          <span className="text-[10px] font-black text-purple-500 uppercase">Credits</span>
                       </div>
                    </div>
                 </div>
             </div>
          </div>
        </div>
      </main>
    </div>
  );
}
