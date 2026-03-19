"use client";

import React, { useState, useEffect, useRef } from 'react';
import { Shield, Zap, Lock, Cpu, Globe, MessageSquare, Terminal, Wallet, Send } from 'lucide-react';

export default function Dashboard() {
  const [messages, setMessages] = useState([
    { role: 'system', content: 'Connection established via Enigma Sovereign Core.' },
    { role: 'assistant', content: 'Greetings Juan. Identity Enigma #1686 synchronized. How can I serve the DOF ecosystem today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

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

      if (!response.ok) throw new Error('Cerebro desconectado');
      
      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (error) {
      setMessages(prev => [...prev, { role: 'system', content: '⚠️ Error: No se pudo conectar con el Cerebro de Enigma. Asegúrate de que el script de activación esté corriendo.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  const [stats, setStats] = useState({ memory_percent: 84, cpu_percent: 42 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await fetch('http://localhost:8005/api/stats');
        if (res.ok) {
           const data = await res.json();
           setStats(data);
        }
      } catch (e) {}
    };
    fetchStats();
    const interval = setInterval(fetchStats, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-[#050505] text-white font-sans selection:bg-purple-500/30">
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-[10%] -left-[10%] w-[40%] h-[40%] bg-purple-900/10 blur-[120px] rounded-full" />
        <div className="absolute top-[20%] -right-[10%] w-[30%] h-[30%] bg-blue-900/10 blur-[120px] rounded-full" />
      </div>

      <nav className="sticky top-0 z-50 border-b border-white/5 bg-black/50 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-br from-purple-500 to-blue-600 rounded-lg flex items-center justify-center">
              <Shield size={18} className="text-white" />
            </div>
            <span className="font-bold tracking-tight text-xl text-white">DOF <span className="text-purple-500 font-black italic">OS</span></span>
          </div>
          <div className="hidden md:flex items-center gap-8 text-sm font-medium text-zinc-400">
            <span className="text-emerald-400">● LIVE</span>
            <span className="cursor-pointer hover:text-white transition-colors">Ecosystem</span>
            <span className="cursor-pointer hover:text-white transition-colors">Skills</span>
            <span className="cursor-pointer hover:text-white transition-colors">x402</span>
          </div>
          <button className="px-4 py-2 bg-white text-black text-sm font-bold rounded-full hover:bg-zinc-200 transition-all active:scale-95">
            M4 MAX: 36GB
          </button>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-6 py-12 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 h-[calc(100vh-200px)]">
          
          <div className="lg:col-span-8 flex flex-col bg-zinc-900/40 border border-white/5 rounded-[32px] overflow-hidden backdrop-blur-md">
             <div className="p-6 border-b border-white/10 flex items-center justify-between bg-white/5">
                <div className="flex items-center gap-3">
                   <div className="w-3 h-3 bg-purple-500 rounded-full animate-pulse" />
                   <h3 className="font-bold tracking-tight">ENIGMA #1686 TERMINAL</h3>
                </div>
                <div className="text-[10px] font-mono text-zinc-500">ENCLAVE_ACTIVE // SECTOR: SYNTHESIS_2026</div>
             </div>

             <div ref={scrollRef} className="flex-1 p-8 space-y-6 overflow-y-auto scroll-smooth">
                {messages.map((m, i) => (
                  <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                    <div className={`max-w-[85%] p-4 rounded-2xl text-sm leading-relaxed ${
                      m.role === 'user' 
                      ? 'bg-purple-600/20 border border-purple-500/30 text-white' 
                      : m.role === 'system'
                      ? 'bg-zinc-800/50 text-zinc-400 font-mono text-[10px]' 
                      : 'bg-white/5 border border-white/10 text-zinc-100 shadow-2xl'
                    }`}>
                      {m.role === 'assistant' && <div className="text-[10px] font-bold text-purple-400 mb-1 tracking-widest uppercase">ENIGMA</div>}
                      {m.content}
                    </div>
                  </div>
                ))}
                {isLoading && (
                  <div className="flex justify-start">
                    <div className="p-4 rounded-xl bg-white/5 flex gap-1 items-center">
                      <div className="w-1.5 h-1.5 bg-zinc-500 rounded-full animate-bounce [animation-delay:-0.3s]" />
                      <div className="w-1.5 h-1.5 bg-zinc-500 rounded-full animate-bounce [animation-delay:-0.15s]" />
                      <div className="w-1.5 h-1.5 bg-zinc-500 rounded-full animate-bounce" />
                    </div>
                  </div>
                )}
             </div>

             <div className="p-6 bg-white/5 border-t border-white/10">
                <div className="relative flex items-center">
                  <input 
                    type="text" 
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                    placeholder="Command Engima..." 
                    className="w-full bg-black/40 border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/50 transition-all backdrop-blur-sm"
                  />
                  <button 
                    onClick={handleSend}
                    disabled={isLoading}
                    className="absolute right-3 p-2 bg-purple-600 rounded-xl hover:bg-purple-500 transition-all disabled:opacity-50"
                  >
                    <Send size={18} />
                  </button>
                </div>
             </div>
          </div>

          <div className="lg:col-span-4 flex flex-col gap-6">
             <div className="bg-zinc-900/40 border border-white/5 rounded-[32px] p-8 backdrop-blur-md">
                <div className="flex items-center gap-3 mb-6 font-bold">
                   <Cpu className="text-purple-500" /> SYSTEM RESOURCES
                </div>
                <div className="space-y-6">
                   <div>
                      <div className="flex justify-between text-xs text-zinc-500 mb-2 font-mono"><span>MEMORY (36GB)</span><span>{Math.round(stats.memory_percent)}%</span></div>
                      <div className="h-1.5 w-full bg-white/10 rounded-full overflow-hidden">
                         <div className="h-full bg-purple-500 shadow-[0_0_10px_#a855f7] transition-all duration-1000" style={{ width: `${stats.memory_percent}%` }} />
                      </div>
                   </div>
                   <div>
                      <div className="flex justify-between text-xs text-zinc-500 mb-2 font-mono"><span>CPU LOAD</span><span>{Math.round(stats.cpu_percent)}%</span></div>
                      <div className="h-1.5 w-full bg-white/10 rounded-full overflow-hidden">
                         <div className="h-full bg-blue-500 shadow-[0_0_10px_#3b82f6] transition-all duration-1000" style={{ width: `${stats.cpu_percent}%` }} />
                      </div>
                   </div>
                </div>
             </div>

             <div className="flex-1 bg-gradient-to-br from-purple-900/20 to-zinc-900/40 border border-purple-500/20 rounded-[32px] p-8 backdrop-blur-md relative overflow-hidden group">
                <Wallet className="absolute -bottom-8 -right-8 w-48 h-48 text-white/5 group-hover:rotate-12 transition-transform duration-700" />
                <h4 className="text-lg font-bold mb-4 flex items-center gap-2 underline decoration-purple-500 underline-offset-4">X402 PROTOCOL</h4>
                <p className="text-xs text-zinc-500 mb-6 leading-relaxed">Agent-to-Agent trustless payments are bridged. x402 is ready for deployment on Avalanche/Celo.</p>
                <div className="grid grid-cols-2 gap-3 text-center">
                   <div className="p-3 bg-white/5 rounded-2xl border border-white/10">
                      <div className="text-[10px] text-zinc-500">LIQUIDITY</div>
                      <div className="text-sm font-black">$00.00</div>
                   </div>
                   <div className="p-3 bg-white/5 rounded-2xl border border-white/10">
                      <div className="text-[10px] text-zinc-500">TRUST SCORE</div>
                      <div className="text-sm font-black text-emerald-400">9.8/10</div>
                   </div>
                </div>
             </div>
          </div>
        </div>
      </main>
    </div>
  );
}
