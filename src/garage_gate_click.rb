#!/usr/bin/ruby

require 'pi_piper'
include PiPiper

relay1 = Pin.new(pin: 24, direction: :out)

relay1.update_value(1)

sleep 0.5

relay1.update_value(0)

