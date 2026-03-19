import os
import subprocess
import logging
import sys

# Configure logging for better observability
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('logs/vercel_sync.log')
    ]
)
logger = logging.getLogger("VercelSync")

def sync_to_vercel():
    """
    Automates the deployment process to Vercel for the DOF Agent Dashboard.
    Ensures the 'hackathon' branch is live and reflects the latest 13-agent swarm state.
    """
    try:
        logger.info("🚀 Starting Vercel Synchronized Deploy...")
        
        # Ensure we are in the right directory (project root)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        frontend_dir = os.path.join(project_root, "frontend")
        
        if not os.path.exists(frontend_dir):
            logger.error(f"Frontend directory not found at {frontend_dir}")
            return False

        # Build command
        # --prod: Deploy to production
        # --yes: Skip confirmation
        # --token: Use VERCEL_TOKEN from environment
        token = os.getenv("VERCEL_TOKEN")
        cmd = ["npx", "-y", "vercel", "--prod", "--yes", "--cwd", frontend_dir]
        
        if token:
            cmd.extend(["--token", token])
            logger.info("Using VERCEL_TOKEN from environment.")
        else:
            logger.warning("VERCEL_TOKEN not found. Deployment might fail if CLI is not logged in.")

        # Execute deployment
        logger.info(f"Executing: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        logger.info("--- Vercel Output ---")
        logger.info(result.stdout)
        logger.info("---------------------")
        
        logger.info("✅ Vercel Sync SUCCESSFUL. Dashboard is LIVE.")
        return True

    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Vercel Sync FAILED (Exit Code {e.returncode})")
        logger.error(f"Error Output: {e.stderr}")
        return False
    except Exception as e:
        logger.error(f"❌ Vercel Sync encountered an UNEXPECTED ERROR: {e}")
        return False

if __name__ == "__main__":
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    success = sync_to_vercel()
    if success:
        print("\n🏆 Vercel Sync Engine: DEPLOYED and Monitoring.")
    else:
        print("\n⚠️ Vercel Sync Engine: Deployment failed. Check logs/vercel_sync.log")
        sys.exit(1)
