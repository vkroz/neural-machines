import torch

"""
See: 
- https://developer.apple.com/metal/pytorch/
- https://developer.apple.com/videos/play/wwdc2024/10160/?time=256
"""

def main():
    if torch.backends.mps.is_available():
        mps_device = torch.device("mps")
        x = torch.ones(1, device=mps_device)
        print (x)
        print ("Successfully created a MPS device.")
    else:
        print ("MPS device not found.")

if __name__ == "__main__":
    main()


    