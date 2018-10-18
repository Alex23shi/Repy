data =
thisdata = data
    while thisdata:
        eightbytesequence = thisdata[:8]
        thisdata = thisdata[8:]
        even = True
        for thisbyte in eightbytesequence:
          # for each byte, if it is odd, flip even to be the opposite
          if ord(thisbyte) % 2:
            even = not even

        # actually call write, if we are supposed to...
        if even:
          self.file.writeat(eightbytesequence,offset)
        # ...or error out.
        else:
          raise RepyParityError("Non-even parity write to file")